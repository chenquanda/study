from ultralytics import YOLO

# Load a COCO-pretrained YOLO26n model
model = YOLO("ai-dev/vision-demo/model/yolo26n.pt")

# Train the model on the COCO8 example dataset for 100 epochs
# results = model(data="coco8.yaml", epochs=100, imgsz=640)

# Run inference with the YOLO26n model on the 'bus.jpg' image
results = model(r"ai-dev/vision-demo/test-img/test01.jpg")

print(results)
