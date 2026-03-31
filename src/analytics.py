class LineCrossCounter:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.crossed_ids = set()
        self.count = 0

    def _get_center(self, bbox):
        x1, y1, x2, y2 = bbox
        return ((x1 + x2) / 2, (y1 + y2) / 2)

    def _is_below_line(self, point):
        x, y = point
        x1, y1 = self.start
        x2, y2 = self.end
        return (x2 - x1) * (y - y1) - (y2 - y1) * (x - x1) > 0

    def update(self, tracks):
        for track in tracks:
            tid = track["track_id"]
            if tid in self.crossed_ids:
                continue
            center = self._get_center(track["bbox"])
            if self._is_below_line(center):
                self.crossed_ids.add(tid)
                self.count += 1

    def get_count(self):
        return self.count