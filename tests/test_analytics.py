from src.analytics import LineCrossCounter


def make_track(track_id, bbox):
    return {"track_id": track_id, "bbox": bbox, "class_id": 2}


def test_no_crossing():
    counter = LineCrossCounter(start=(0, 360), end=(1280, 360))
    tracks = [make_track(1, [100, 100, 200, 200])]
    counter.update(tracks)
    assert counter.get_count() == 0


def test_single_crossing():
    counter = LineCrossCounter(start=(0, 360), end=(1280, 360))
    tracks = [make_track(1, [100, 400, 200, 500])]
    counter.update(tracks)
    assert counter.get_count() == 1


def test_no_double_counting():
    counter = LineCrossCounter(start=(0, 360), end=(1280, 360))
    track = [make_track(1, [100, 400, 200, 500])]
    counter.update(track)
    counter.update(track)
    counter.update(track)
    assert counter.get_count() == 1


def test_multiple_vehicles():
    counter = LineCrossCounter(start=(0, 360), end=(1280, 360))
    counter.update([make_track(1, [100, 400, 200, 500])])
    counter.update([make_track(2, [300, 400, 400, 500])])
    counter.update([make_track(3, [500, 400, 600, 500])])
    assert counter.get_count() == 3


def test_above_line_not_counted():
    counter = LineCrossCounter(start=(0, 360), end=(1280, 360))
    tracks = [
        make_track(1, [100, 400, 200, 500]),
        make_track(2, [100, 100, 200, 200]),
    ]
    counter.update(tracks)
    assert counter.get_count() == 1
