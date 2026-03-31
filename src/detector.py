import yaml
from ultralytics import YOLO


class Detector:
    def __init__(self, config_path="configs/default.yaml"):
        with open(config_path, "r") as f:
            cfg = yaml.safe_load(f)

        model_cfg = cfg["model"]
        self.model = YOLO(model_cfg["weights"])
        self.confidence = model_cfg["confidence"]
        self.iou_threshold = model_cfg["iou_threshold"]
        self.classes = model_cfg["classes"]

    def detect(self, frame):
        results = self.model(
            frame,
            conf=self.confidence,
            iou=self.iou_threshold,
            classes=self.classes,
            verbose=False
        )

        detections = []
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                conf = float(box.conf[0])
                cls = int(box.cls[0])
                label = self.model.names[cls]
                detections.append({
                    "bbox": [x1, y1, x2, y2],
                    "confidence": conf,
                    "class_id": cls,
                    "label": label
                })

        return detections