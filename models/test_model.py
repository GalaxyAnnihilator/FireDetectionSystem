import cv2, os
from ultralytics import YOLO

folder_path = "./models"
pt_files = [f for f in os.listdir(folder_path) if f.endswith('.pt')]

print("Choose your model to run: ")
for i, model_name in enumerate(pt_files):
    print(f"{i+1}. {model_name}")

choice = int(input("Your choice is: "))
if choice is None:
    choice = 1  # default choice

model = YOLO(f"./models/{pt_files[choice - 1]}")

cap = cv2.VideoCapture(0)

# Read first frame and convert to grayscale
ret, prev_frame = cap.read()
prev_gray = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    diff = cv2.absdiff(prev_gray, gray)
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        if cv2.contourArea(cnt) < 500:  # skip small movements
            continue

        x, y, w, h = cv2.boundingRect(cnt)
        roi = frame[y:y+h, x:x+w]

        # Run YOLO only on the ROI
        results = model(roi, stream=True, conf=0.4)

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                conf = float(box.conf[0])
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                # Adjust coordinates relative to full frame
                x1 += x
                x2 += x
                y1 += y
                y2 += y

                label = f"{model.names[cls_id]} {conf:.2f}"
                color = (0, 0, 255) if "fire" in model.names[cls_id].lower() else (0, 255, 0)

                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    cv2.imshow("Motion-based Detection", frame)
    prev_gray = gray.copy()

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()
