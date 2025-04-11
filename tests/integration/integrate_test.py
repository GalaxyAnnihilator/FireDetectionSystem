import unittest
import cv2
import os
from deployment.predict import FireDetector

class TestFireDetectionIntegration(unittest.TestCase):
    def setUp(self):
        """Set up the FireDetector instance and output log file."""
        self.detector = FireDetector(model_path='../models/best.pt')
        self.test_videos_dir = '../tests/unit/'  # Directory containing test videos
        self.output_log = '../tests/integration/output_log.txt'

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
        """Process a video and check if fire is detected."""
        cap = cv2.VideoCapture(video_path)
        fire_detected = False

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            _, frame_fire_detected = self.detector.process_frame(frame)
            if frame_fire_detected:
                fire_detected = True
                break

        cap.release()
        return fire_detected

    def _log_result(self, video_file, fire_detected):
        """Log the result of fire detection for a video."""
        result = f"{video_file}: {'Fire Detected' if fire_detected else 'No Fire Detected'}\n"
        with open(self.output_log, 'a') as log_file:
            log_file.write(result)

if __name__ == '__main__':
    unittest.main()
