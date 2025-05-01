from ultralytics import YOLO

model = YOLO("yolov8s.pt")  # Load a pretrained model (or specify a custom path)

model.train(data="data.yaml", epochs=6 , device='cuda')  # Train the model on the COCO128 dataset for 3 epochs