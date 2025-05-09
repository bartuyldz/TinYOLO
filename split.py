import os
import shutil
import random

# Fotoğrafların bulunduğu klasör
source_folder = './images/YELLOW'  # Burayı kendi klasör yolunla değiştir
train_folder = './images/train'
val_folder = './images/val'


# Fotoğrafların listesini al
all_files = [f for f in os.listdir(source_folder) if f.endswith(('.jpg', '.png', '.jpeg'))]

# Fotoğrafları karıştır
random.shuffle(all_files)

# Eğitim ve doğrulama setlerine ayırma
train_count = int(len(all_files) * 0.8)
val_count = len(all_files) - train_count

# Eğitim setine dosya kopyalama
for file in all_files[:train_count]:
    shutil.copy(os.path.join(source_folder, file), os.path.join(train_folder, file))

# Doğrulama setine dosya kopyalama
for file in all_files[train_count:]:
    shutil.copy(os.path.join(source_folder, file), os.path.join(val_folder, file))

print(f"{train_count} dosya train setine, {val_count} dosya val setine kopyalandı.")
