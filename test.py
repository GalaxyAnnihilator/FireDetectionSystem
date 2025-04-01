import time
import os
import cv2
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('best.pt')  # Đảm bảo model đã được huấn luyện để nhận diện class "fire"

# Init variables
cap = cv2.VideoCapture(0)
fire_detected_time = None
fire_detection_threshold = 5  # Phát hiện cháy liên tục bao nhiêu giây thì báo động
start = time.time()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    current_time = time.time()
    timer = current_time - start

    # Thực hiện dự đoán mỗi 0.5s
    if timer >= 0.1:
        results = model.predict(source=frame, imgsz=640, conf=0.4, save_conf=False, verbose=False)
        fire_found = False

        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                label = model.names[cls_id]

                x1, y1, x2, y2 = map(int, box.xyxy[0])
                color = (0, 0, 255) if label.lower() == 'fire' else (0, 255, 0)
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, f"{label}: {conf:.2f}", (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)

                if label.lower() == 'fire':
                    fire_found = True

        if fire_found:
            if fire_detected_time is None:
                fire_detected_time = current_time
            print("FIREEEEEE!")

            if current_time - fire_detected_time >= fire_detection_threshold:
                print("FIREEEEEE! Emergency triggered!")
                cap.release()
                cv2.destroyAllWindows()
                # os.system("afplay /Users/thanhlamng/Downloads/FIRE/chay.mp3 & sleep 10; kill $!")  # macOS
                exit()
        else:
            fire_detected_time = None

        start = current_time  # reset timer

    # Show frame
    cv2.imshow("YOLOv8 Fire Detection", frame)
    if cv2.waitKey(1) == 32:  # Nhấn phím cách để thoát
        break

cap.release()
cv2.destroyAllWindows()