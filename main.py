import time
import cv2
from ultralytics import YOLO

# Load model
print("Loading YOLOv8 model...")
model = YOLO('best.pt')

# Open camera
cap = cv2.VideoCapture(0)
start = time.time()

# Nhận diện tên lớp từ model
class_names = model.names  # dictionary: {0: 'label1', 1: 'label2', ...}

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Dự đoán
    results = model.predict(source=frame, imgsz=640, conf=0.1, verbose=False)

    end = time.time()
    timer = end - start
    print("YOLOv8 Execution time:", round(timer, 3), "s")
    start = time.time()

    # Vẽ kết quả
    for result in results:
        boxes = result.boxes
        for box in boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])  # bounding box
            conf = float(box.conf[0])               # độ tin cậy
            cls_id = int(box.cls[0])                # class ID
            label = class_names[cls_id]

            # Vẽ khung và nhãn
            color = (0, 255, 0)
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, f"{label} {conf:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

    # Hiển thị ảnh
    cv2.imshow("YOLOv8 Object Detection", frame)

    # Nhấn phím SPACE để thoát
    if cv2.waitKey(1) == 32:
        break

# Giải phóng tài nguyên
cap.release()
cv2.destroyAllWindows()