import os
import urllib.parse

# Nerede label dosyaları varsa
label_folder = 'labels'
renamed = 0

for filename in os.listdir(label_folder):
    if not filename.endswith('.txt'):
        continue

    # Orijinal isim: b1afe73d__Users%5CBartu%5CDESKTOP%5C...%5CIMG_2655.jpg.txt
    parts = filename.split('__')
    if len(parts) != 2:
        continue

    encoded_path = parts[1].replace('.txt', '')  # %5CIMG_2655.jpg
    decoded_path = urllib.parse.unquote(encoded_path)  # IMG_2655.jpg

    basename = os.path.basename(decoded_path)  # IMG_2655.jpg
    name_only = os.path.splitext(basename)[0]  # IMG_2655

    new_filename = f"{name_only}.txt"
    os.rename(
        os.path.join(label_folder, filename),
        os.path.join(label_folder, new_filename)
    )
    renamed += 1

print(f"{renamed} label dosyası yeniden adlandırıldı.")
