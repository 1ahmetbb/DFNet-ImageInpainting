import torch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms
import cv2
import os
from DFNet_model import DFNet

# Transform
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Resize((256, 256))
])

# Dataset
class ImageInpaintingDataset(Dataset):
    def __init__(self, original_dir, masked_dir, transform=None):
        self.original_images = sorted(os.listdir(original_dir))
        self.masked_images = sorted(os.listdir(masked_dir))
        self.original_dir = original_dir
        self.masked_dir = masked_dir
        self.transform = transform

    def __len__(self):
        return len(self.original_images)

    def __getitem__(self, idx):
        original_path = os.path.join(self.original_dir, self.original_images[idx])
        masked_path = os.path.join(self.masked_dir, self.masked_images[idx])

        original = cv2.imread(original_path)
        masked = cv2.imread(masked_path)

        original = cv2.cvtColor(original, cv2.COLOR_BGR2RGB)
        masked = cv2.cvtColor(masked, cv2.COLOR_BGR2RGB)

        if self.transform:
            original = self.transform(original)
            masked = self.transform(masked)

        return masked, original

# Veri yolu
original_dir = "path_to_original_images"
masked_dir = "path_to_masked_images"

dataset = ImageInpaintingDataset(original_dir, masked_dir, transform=transform)
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)

# Model, loss, optimizer
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = DFNet().to(device)
criterion = torch.nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Eğitim
for epoch in range(10):
    running_loss = 0.0
    for masked_imgs, original_imgs in dataloader:
        masked_imgs, original_imgs = masked_imgs.to(device), original_imgs.to(device)

        outputs = model(masked_imgs)
        loss = criterion(outputs, original_imgs)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    print(f"Epoch [{epoch+1}/10], Loss: {running_loss / len(dataloader)}")

torch.save(model.state_dict(), "trained_dfnet.pth")