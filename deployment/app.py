import time
import cv2
from predict import FireDetector
from telenoti import send_telegram_message, send_telegram_image

def main():
    detector = FireDetector()
    cap = cv2.VideoCapture(0)
    frame_counter = 0  # Track the number of processed frames

    print("Starting fire detection system...")
    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            # Process frame
            processed_frame, fire_detected = detector.process_frame(frame)
            
            if fire_detected:
                print(f"Fire detected! Sending alert after {12 - frame_counter%12} frames.")
                # Save the frame as an image
                cv2.imwrite("fire_detected.jpg", processed_frame)
                frame_counter += 1
                if frame_counter % 12 == 0:  # Send fire alarm every 5 out of 60 frames
                    send_telegram_message("Fire detected! Please check immediately.")
                    send_telegram_image("fire_detected.jpg")
            
            # Display the frame
            cv2.imshow("Fire Detection System", processed_frame)

            # Handle keyboard input
            key = cv2.waitKey(1)
            if key == 32:  # Space bar to stop
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("System shutdown successfully")

if __name__ == "__main__":
    main()