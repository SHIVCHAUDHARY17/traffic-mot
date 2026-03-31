import cv2
import yaml
from src.detector import Detector
from src.tracker import Tracker
from src.analytics import LineCrossCounter
from src.annotator import draw_tracks, draw_counting_line


class Pipeline:
    def __init__(self, config_path="configs/default.yaml"):
        with open(config_path) as f:
            self.cfg = yaml.safe_load(f)

        self.detector = Detector(config_path)
        self.tracker = Tracker()

        line_cfg = self.cfg["analytics"]["counting_line"]
        self.line_start = line_cfg["start"]
        self.line_end = line_cfg["end"]
        self.counting_enabled = line_cfg["enabled"]

    def run(self):
        source = self.cfg["video"]["source"]
        output = self.cfg["video"]["output"]

        cap = cv2.VideoCapture(source)
        if not cap.isOpened():
            raise RuntimeError(f"Cannot open video: {source}")

        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = cap.get(cv2.CAP_PROP_FPS)
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(output, fourcc, fps, (w, h))

        start_px = (int(self.line_start[0] * w), int(self.line_start[1] * h))
        end_px = (int(self.line_end[0] * w), int(self.line_end[1] * h))
        counter = LineCrossCounter(start_px, end_px)

        frame_idx = 0
        print(f"Processing {total} frames...")

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            detections = self.detector.detect(frame)
            tracks = self.tracker.update(detections, frame)

            if self.counting_enabled:
                counter.update(tracks)

            frame = draw_tracks(frame, tracks)

            if self.counting_enabled:
                frame = draw_counting_line(
                    frame, self.line_start, self.line_end, counter.get_count()
                )

            writer.write(frame)
            frame_idx += 1

            if frame_idx % 30 == 0:
                print(f"  Frame {frame_idx}/{total} — count: {counter.get_count()}")

        cap.release()
        writer.release()
        print(f"Done. Total vehicles counted: {counter.get_count()}")
        print(f"Output saved to: {output}")
