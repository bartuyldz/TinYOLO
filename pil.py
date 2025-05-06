import os
from PIL import Image
import shutil

image_dir = "images/val"  # veya val/test


for filename in os.listdir(image_dir):
    if filename.lower().endswith(".jpg"):
        base = os.path.splitext(filename)[0]
        img_path = os.path.join(image_dir, filename)

        # Yeni isim
        new_img_path = os.path.join(image_dir, base + ".jpeg")

        try:
            # Görseli yeniden kaydet
            img = Image.open(img_path).convert("RGB")
            img.save(new_img_path, "JPEG", quality=95)
            os.remove(img_path)

        except Exception as e:
            print(f"{filename} hatalı: {e}")
