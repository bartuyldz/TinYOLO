import os
import shutil

# Klasör yollarını ayarla
images_train_dir = 'images/train'
images_val_dir = 'images/val'
labels_src_dir = 'labels'  # label dosyalarının hepsi burada
labels_train_dir = 'labels/train'
labels_val_dir = 'labels/val'

# Hedef klasörler varsa silinmesin ama yoksa oluşturulsun
os.makedirs(labels_train_dir, exist_ok=True)
os.makedirs(labels_val_dir, exist_ok=True)

def move_labels(image_dir, label_dest_dir):
    for filename in os.listdir(image_dir):
        name, ext = os.path.splitext(filename)
        if ext.lower() not in ['.jpg', '.jpeg', '.png']:
            continue  # Görsel değilse atla

        label_file = name + '.txt'
        src_path = os.path.join(labels_src_dir, label_file)
        dest_path = os.path.join(label_dest_dir, label_file)

        if os.path.exists(src_path):
            shutil.copyfile(src_path, dest_path)
            print(f"Kopyalandı: {label_file}")
        else:
            print(f"UYARI: Etiket bulunamadı -> {label_file}")

# Train ve val için uygula
move_labels(images_train_dir, labels_train_dir)
move_labels(images_val_dir, labels_val_dir)
