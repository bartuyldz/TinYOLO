import cv2
from ultralytics import YOLO

# Modeli yükle
model = YOLO("runs/detect/train16/weights/best.pt")

# Webcam'i başlat (0 genellikle varsayılan kameradır)
cap = cv2.VideoCapture(0)

def sendID(classID):
    return class_id

while True:
    # Kameradan bir kare oku
    ret, frame = cap.read()

    # Okuma başarılı olduysa
    if ret:
        # YOLOv8 ile tahmini gerçekleştir
        results = model.predict(frame, stream=True, conf=0.72, iou=0.4)  # stream=True ile gerçek zamanlı tahmin yapıyoruz

        # Sonuçları işle
        for r in results:
            boxes = r.boxes
            for box in boxes:
                # Bounding box koordinatları
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                w, h = x2 - x1, y2 - y1

                # Güven skoru
                conf = box.conf[0]

                # Sınıf indeksi
                cls = int(box.cls[0])

                # Sınıf adı
                class_name = model.names[cls]

                # Sınıf ID'si
                class_id = int(box.cls[0])

                sendID(class_id)

                if conf > 0.5:  # İsteğe bağlı: Sadece belirli bir güven skorunun üzerindeki tespitleri göster
                    # Bounding box'ı çiz
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

                    # Etiketi oluştur
                    label = f'{class_name},{class_id} : {conf:.2f}'
                    # Etiketi çiz
                    cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # İşlenmiş kareyi göster
        cv2.imshow('YOLOv8 Real-time Detection', frame)

        # 'q' tuşuna basıldığında döngüden çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# Kamerayı serbest bırak ve pencereleri kapat
cap.release()
cv2.destroyAllWindows()