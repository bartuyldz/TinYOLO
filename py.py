import os
import urllib.parse

# Label dosyalarının bulunduğu klasör
label_folder = 'labels'
renamed = 0
skipped = 0

for filename in os.listdir(label_folder):
    if not filename.endswith('.txt'):
        continue

    # Dosya adı çözümlemesi
    parts = filename.split('__')
    if len(parts) != 2:
        continue

    encoded_path = parts[1] # URL encoded kısmı alıyoruz
    decoded_path = urllib.parse.unquote(encoded_path)  # URL çözümlemesi yapılıyor

    basename = os.path.basename(decoded_path)  # WIN_20250506_23_46_45_Pro (2).txt

    # Yeni dosya adı, .txt uzantısı korunuyor
    new_filename = basename  # Pro kısmı korunuyor

    old_path = os.path.join(label_folder, filename)
    new_path = os.path.join(label_folder, new_filename)

    # Dosya zaten varsa atlanır
    if os.path.exists(new_path):
        print(f"Atlandı (zaten var): {new_filename}")
        skipped += 1
        continue

    os.rename(old_path, new_path)
    print(f"Yeniden adlandırıldı: {filename} → {new_filename}")
    renamed += 1

print(f"\n{renamed} dosya yeniden adlandırıldı, {skipped} dosya atlandı (zaten vardı).")
