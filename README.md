# **DFNet Görüntü Inpainting Projesi**

Bu proje, **derin öğrenme tabanlı görüntü inpainting** (eksik bölge doldurma) amacıyla geliştirilmiştir. DFNet modeli kullanarak **maskelenmiş (eksik bölge içeren) görüntülerin kayıp kısımlarını tahmin eder** ve tam bir görüntü oluşturur.

---

## **Proje İçeriği**

1. **DFNet Modeli:** Encoder-Decoder mimarisine dayalı basit bir model.
2. **Veri Ön İşleme:** Resimlere rastgele elips maskeler uygulanır.
3. **Model Eğitimi:** Maskelenmiş resimler kullanılarak model eğitilir.
4. **Model Testi:** Eğitilmiş model ile maskelenmiş resimlerin maskesiz halleri tahmin edilir.

---

## **Kullanılan Teknolojiler**

- **Python 3.**
- **PyTorch** (Derin Öğrenme Kütüphanesi)
- **OpenCV** (Görüntü İşleme)
- **Matplotlib** (Sonuçları Görselleştirme)

---

## **Kurulum Adımları**

1. **Proje Depolarını Klonlayın:**
   ```bash
   git clone https://github.com/1ahmetbb/DFNet-ImageInpainting
   cd DFNet-ImageInpainting

2.	**Gerekli Kütüphaneleri Kurun:**
```bash
    pip install -r requirements.txt
```

4.	**Veri Setini Hazırlayın:**
	•	Orijinal resimlerinizi bir klasöre koyun. Örneğin: data/original_images
	•	Maskelenmiş resimlerinizi oluşturmak için train.py içinde mask_and_save_images fonksiyonunu kullanın.

5.	**Modeli Eğitme:**
Aşağıdaki komutla modeli eğitebilirsiniz:
```bash
    python train.py
```
    •	Eğitilmiş model ağırlıkları trained_dfnet.pth dosyasına kaydedilir.
	
6.	**Modeli Test Etme:**
Eğitilmiş modeli kullanarak yeni maskelenmiş resimlerin maskesiz hallerini tahmin etmek için
```bash
    python test.py
```

## **Proje Kullanımı**

1. **Modeli Eğitim İçin:**

	•	Orijinal ve maskelenmiş resimleri kullanarak modeli eğitin:
```bash
    python train.py
```
2. **Modeli Test İçin:**
	•	Yeni maskelenmiş bir görüntüyü test edin:
```bash
    python test.py
```
## **Gereksinimler**

Proje için gerekli kütüphaneleri kurmak için aşağıdaki dosyayı kullanabilirsiniz:

torch
torchvision
opencv-python
matplotlib


## **Eğitilmiş Model Ağırlıkları**

Eğitilmiş model ağırlıklarını trained_dfnet.pth dosyasından yükleyebilirsiniz. Bu dosya, eğitilmiş DFNet modelini içerir ve yeniden eğitim gerektirmez.


## **Gelecek Geliştirmeler**
	•	Farklı veri setleri ile modelin performansını artırmak.
	•	Daha karmaşık maskeler kullanmak (örneğin, serbest çizim maskeleri).
	•	Modeli daha büyük veri setleri üzerinde eğitmek.

## **Katkıda Bulunma**

**Katkıda bulunmak için:**	
1.	Bu depoyu fork edin.
2.	Yeni bir özellik ekleyin veya bir hatayı düzeltin.
3.	PR (Pull Request) gönderin.

## **Lisans**

Bu proje MIT lisansı altında yayınlanmıştır.
