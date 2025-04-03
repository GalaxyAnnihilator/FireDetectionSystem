import time
import cv2
from predict import FireDetector

class Application:
    def __init__(self):
        self.detector = FireDetector()
        self.cap = cv2.VideoCapture(0)
        self.running = True
        self.fps_history = []

    def run(self):
        """Main application loop"""
        print("Starting fire detection system...")
        start_time = time.time()
        
        try:
            while self.running and self.cap.isOpened():
                ret, frame = self.cap.read()
                if not ret:
                    break

                # Process frame
                processed_frame, fire_detected = self.detector.process_frame(frame)
                
                # Calculate FPS
                fps = self._calculate_fps(start_time)
                self._display_stats(processed_frame, fps, fire_detected)
                
                # Show output
                cv2.imshow("Fire Detection System", processed_frame)
                self._handle_input()

        finally:
            self._cleanup()

    def _calculate_fps(self, start_time):
        """Calculate and smooth FPS values"""
        elapsed = time.time() - start_time
        fps = 1 / elapsed
        self.fps_history = (self.fps_history + [fps])[-10:]  # Keep last 10 values
        return sum(self.fps_history)/len(self.fps_history)

    def _display_stats(self, frame, fps, fire_detected):
        """Display system statistics on frame"""
        status_color = (0, 0, 255) if fire_detected else (0, 255, 0)
        status_text = "FIRE DETECTED!" if fire_detected else "System Normal"
        
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        cv2.putText(frame, status_text, (10, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, status_color, 2)

    def _handle_input(self):
        """Handle keyboard input"""
        key = cv2.waitKey(1)
        if key == 32:  # Space bar
            self.running = False
        elif key == ord('f'):  # Toggle fullscreen
            cv2.setWindowProperty("Fire Detection System", cv2.WND_PROP_FULLSCREEN,
                                not cv2.getWindowProperty("Fire Detection System", cv2.WND_PROP_FULLSCREEN))

    def _cleanup(self):
        """Release resources"""
        self.cap.release()
        cv2.destroyAllWindows()
        print("System shutdown successfully")

if __name__ == "__main__":
    app = Application()
    app.run()