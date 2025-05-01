from ultralytics import YOLO
model = YOLO('runs/detect/train2/weights/best.pt')
results = model('test_image1.jpg', conf=0.3, show=True)
