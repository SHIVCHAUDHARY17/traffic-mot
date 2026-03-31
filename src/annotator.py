import cv2

COLORS = [
    (255, 100, 100), (100, 255, 100), (100, 100, 255),
    (255, 255, 100), (255, 100, 255), (100, 255, 255),
    (255, 165, 0),   (0, 255, 127),   (238, 130, 238),
]

CLASS_NAMES = {2: "car", 3: "motorcycle", 5: "bus", 7: "truck"}


def get_color(track_id):
    return COLORS[track_id % len(COLORS)]


def draw_tracks(frame, tracks):
    for track in tracks:
        tid = track["track_id"]
        x1, y1, x2, y2 = [int(v) for v in track["bbox"]]
        color = get_color(tid)
        label = CLASS_NAMES.get(track["class_id"], "vehicle")

        cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
        text = f"ID:{tid} {label}"
        (tw, th), _ = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 0.5, 1)
        cv2.rectangle(frame, (x1, y1 - th - 6), (x1 + tw + 4, y1), color, -1)
        cv2.putText(frame, text, (x1 + 2, y1 - 4),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)

    return frame


def draw_counting_line(frame, start, end, count):
    h, w = frame.shape[:2]
    x1 = int(start[0] * w)
    y1 = int(start[1] * h)
    x2 = int(end[0] * w)
    y2 = int(end[1] * h)

    cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
    cv2.putText(frame, f"Count: {count}", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

    return frame