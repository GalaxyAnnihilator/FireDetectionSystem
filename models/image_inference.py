from ultralytics import YOLO
import cv2

# Load model
model = YOLO("./models/bestOftheBes.pt")

# Load image
image_path = "./models/image.png"
img = cv2.imread(image_path)

# Run inference
results = model(img)

# Visualize results
annotated_frame = results[0].plot()
cv2.imwrite("result.png", annotated_frame)
