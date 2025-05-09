import cv2
import serial
import time
from ultralytics import YOLO

# Serial portu ayarla
ser = serial.Serial('COM3', 115200, timeout=1)  # timeout = bekleme süresi
time.sleep(2)  # Pico'nun başlatılması için bekle

# YOLO modeli yükle
model = YOLO("runs/detect/train16/weights/best.pt")
cap = cv2.VideoCapture(0)

def sendIDAndWait(class_id):
    try:
        ser.write(f"{class_id}\n".encode())
        print("Gönderildi:", class_id)

        # Pico'dan yanıt bekle
        while True:
            if ser.in_waiting > 0:
                response = ser.readline().decode().strip()
                print("Pico'dan gelen:", response)
                if response == "NEXT":
                    break
    except Exception as e:
        print("Hata:", e)

while True:
    ret, frame = cap.read()

    if ret:
        results = model.predict(frame, stream=True, conf=0.72, iou=0.4)

        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = box.conf[0]
                class_id = int(box.cls[0])
                if conf > 0.5:
                    sendIDAndWait(class_id)  #Gönder, sonra Pico'dan tetik bekle

                    # Etiketi çiz
                    label = f'{model.names[class_id]} ({class_id})'
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(frame, label, (x1, y1 - 10),
                                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        cv2.imshow('YOLOv8', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
ser.close()
