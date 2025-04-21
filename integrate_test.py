import unittest
import cv2
import os
from deployment.predict import FireDetector

class TestFireDetectionIntegration(unittest.TestCase):
    def setUp(self):
        """Set up the FireDetector instance and output log file."""
        self.detector = FireDetector(model_path='./models/bestOftheBes.pt')
        self.test_videos_dir = './tests/unit/'  # Directory containing test videos
        self.output_log = './tests/integration/output_log.txt'

        # Clear the log file before starting tests
        with open(self.output_log, 'w') as log_file:
            log_file.write("Fire Detection Test Results:\n")

    def test_video_fire_detection(self):
        """Test fire detection on all videos in the test directory."""
        for video_file in os.listdir(self.test_videos_dir):
            if video_file.endswith('.mp4') or video_file.endswith('.avi'):
                video_path = os.path.join(self.test_videos_dir, video_file)
                fire_detected = self._process_video(video_path)
                self._log_result(video_file, fire_detected)

    def _process_video(self, video_path):
        """Process a video, show it in real-time, and save the output."""
        cap = cv2.VideoCapture(video_path)
        fire_detected = False

        # Get video properties
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')

        # Create output path
        video_filename = os.path.basename(video_path)
        output_path = os.path.join('./tests/integration/processed_videos', f'processed_{video_filename}')
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            processed_frame, frame_fire_detected = self.detector.process_frame(frame)

            # Show the processed frame
            cv2.imshow("Fire Detection", processed_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Write the frame to the output video
            out.write(processed_frame)

            if frame_fire_detected:
                fire_detected = True
                break

        cap.release()
        out.release()
        cv2.destroyAllWindows()
        return fire_detected

    def _log_result(self, video_file, fire_detected):
        """Log the result of fire detection for a video."""
        result = f"{video_file}: {'Fire Detected' if fire_detected else 'No Fire Detected'}\n"
        with open(self.output_log, 'a') as log_file:
            log_file.write(result)

if __name__ == '__main__':
    unittest.main()
