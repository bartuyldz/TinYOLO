from ultralytics import YOLO

if __name__ == '__main__':
    model = YOLO("yolov8n.pt")  # veya kullandığın model
    model.train(
        data="data.yaml", 
        epochs=100, 
        imgsz=1280, 
        lr0=0.001, 
        batch=4, 
        patience=20, 
        hsv_h=0, 
        hsv_s=0, 
        hsv_v=0,
        freeze=10,
        device=0 # GPU numarasını belirtmek için kullanabilirsin (0, 1, 2, ...)
    )
