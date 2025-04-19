import cv2, os
from ultralytics import YOLO

folder_path = "./models"
pt_files = [f for f in os.listdir(folder_path) if f.endswith('.pt')]

print("Choose your model to run: ")
for i,model in enumerate(pt_files):
    print(f"{i+1}. {model}")

choice = int(input("Your choice is: "))
if choice is None: 
    choice = 1 #default choice

model = YOLO(f"./models/{pt_files[choice-1]}")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame,stream=True,conf=0.4)

    for r in results:
        boxes = r.boxes
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            x1,y1,x2,y2 = map(int,box.xyxy[0])

            label = f"{model.names[cls_id]} {conf:.2f}"
            color = (0,0,255) if "fire" in model.names[cls_id].lower() else (0,255,0)

            cv2.rectangle(frame,(x1,y1),(x2,y2),color,2)
            cv2.putText(frame,label,(x1,y1-10),cv2.FONT_HERSHEY_SIMPLEX,0.6,color,2)

    cv2.imshow("Fire Detection", frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
cv2.destroyAllWindows()