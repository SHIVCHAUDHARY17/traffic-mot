import numpy as np
from boxmot import ByteTrack


class Tracker:
    def __init__(self):
        self.tracker = ByteTrack()

    def update(self, detections, frame):
        if len(detections) == 0:
            return []

        dets = np.array([
            [*d["bbox"], d["confidence"], d["class_id"]]
            for d in detections
        ], dtype=float)

        tracks = self.tracker.update(dets, frame)
        results = []
        for track in tracks:
            x1, y1, x2, y2, track_id, conf, cls, _ = track
            results.append({
                "track_id": int(track_id),
                "bbox": [x1, y1, x2, y2],
                "confidence": float(conf),
                "class_id": int(cls)
            })

        return results