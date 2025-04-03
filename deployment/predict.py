import cv2
from ultralytics import YOLO

class FireDetector:
    def __init__(self, model_path='models/best.pt'):
        self.model = YOLO(model_path)
        self.class_names = self.model.names
        self.conf_threshold = 0.4

    def process_frame(self, frame):
        """Process a single frame and return annotated frame + fire status"""
        results = self.model.predict(
            source=frame,
            imgsz=640,
            conf=self.conf_threshold,
            verbose=False
        )
        
        fire_detected = False
        annotated_frame = frame.copy()
        
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                conf = float(box.conf[0])
                cls_id = int(box.cls[0])
                
                if self.class_names[cls_id] == 'fire':
                    fire_detected = True
                    self._draw_boxes(annotated_frame, x1, y1, x2, y2, conf)
        
        return annotated_frame, fire_detected

    def _draw_boxes(self, frame, x1, y1, x2, y2, conf):
        """Helper method to draw bounding boxes"""
        color = (0, 255, 0)  # Green for fire
        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        cv2.putText(frame, f"Fire {conf:.2f}", (x1, y1 - 10),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)