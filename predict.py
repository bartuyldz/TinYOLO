from ultralytics import YOLO

# Daha önce eğittiğiniz veya yüklediğiniz modeli yükleyin
model = YOLO("runs/detect/train16/weights/best.pt")  # Eğer en iyi ağırlıklarınız "best.pt" olarak kaydedildiyse

# Tahmin yapmak istediğiniz görüntü dosyasının yolunu belirtin
image_path = "test_image1.JPG"

# Model üzerinde tahmini çalıştırın
results = model.predict(image_path)

# Sonuçları inceleyin
for result in results:
    boxes = result.boxes  # Tespit edilen nesnelerin kutuları
    masks = result.masks  # Segmentasyon maskeleri (varsa)
    probs = result.probs  # Sınıflandırma olasılıkları (varsa)

    # Tespit edilen nesnelerin koordinatları ve sınıf etiketleri
    for box in boxes:
        x1, y1, x2, y2 = box.xyxy[0]
        confidence = box.conf[0]
        class_id = int(box.cls[0])
        class_name = model.names[class_id]
        print(f"Nesne: {class_name}, Güven: {confidence:.2f}, Koordinatlar: ({x1:.0f}, {y1:.0f}), ({x2:.0f}, {y2:.0f})")

    # (İsteğe bağlı) Tespit edilen nesnelerin üzerine kutuları ve etiketleri çizerek görselleştirebilirsiniz
    # Örneğin:
    import cv2
    img = cv2.imread(image_path)
    for box in boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img, f'{model.names[int(box.cls[0])]}: {box.conf[0]:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.imshow("Tahmin Sonucu", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()