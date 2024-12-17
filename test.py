import torch
import cv2
import matplotlib.pyplot as plt
from DFNet_model import DFNet

# Model yükleme
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = DFNet().to(device)
model.load_state_dict(torch.load("trained_dfnet.pth", map_location=device))
model.eval()

# Resim yolu
test_image_path = "path_to_masked_image.jpg"

# Test resmi yükle
test_image = cv2.imread(test_image_path)
test_image = cv2.cvtColor(test_image, cv2.COLOR_BGR2RGB) / 255.0
test_image = torch.tensor(test_image, dtype=torch.float32).permute(2, 0, 1).unsqueeze(0).to(device)

# Tahmin
with torch.no_grad():
    output = model(test_image)

output_img = output.squeeze().permute(1, 2, 0).cpu().numpy()
plt.imshow(output_img)
plt.axis('off')
plt.title("Tamamlanmış Görüntü")
plt.show()