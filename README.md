\# Traffic Multi-Object Tracking



Real-time multi-object tracking pipeline for traffic videos using YOLOv8 and ByteTrack.

Detects and tracks vehicles across frames with persistent IDs and counts vehicles crossing a virtual line.



!\[CI](https://github.com/SHIVCHAUDHARY17/traffic-mot/actions/workflows/ci.yml/badge.svg)



\---



\## What this project does



\- Detects vehicles (car, motorcycle, bus, truck) in traffic video using YOLOv8

\- Assigns persistent track IDs across frames using ByteTrack

\- Counts vehicles crossing a configurable virtual line

\- Outputs annotated video with bounding boxes, class labels, track IDs, and live count



\---



\## Pipeline architecture

```

Traffic video → YOLO detector → ByteTrack → Line counter → Annotated output video

```



\---



\## Project structure

```

traffic-mot/

├── src/

│   ├── detector.py      # YOLOv8 wrapper — per-frame detection

│   ├── tracker.py       # ByteTrack wrapper — persistent track IDs

│   ├── analytics.py     # Line crossing counter

│   ├── annotator.py     # Frame drawing — boxes, IDs, count overlay

│   └── pipeline.py      # End-to-end orchestrator

├── configs/

│   └── default.yaml     # All settings — model, thresholds, line position

├── tests/

│   └── test\_analytics.py  # pytest unit tests

├── .github/workflows/

│   └── ci.yml           # GitHub Actions CI

└── run\_tracker.py       # CLI entry point

```



\---



\## Setup

```bash

git clone https://github.com/SHIVCHAUDHARY17/traffic-mot.git

cd traffic-mot

python -m venv venv

source venv/bin/activate        # Windows: venv\\Scripts\\activate

pip install -r requirements.txt

```



\---



\## Usage



Place your traffic video in `data/` and run:

```bash

python run\_tracker.py --config configs/default.yaml

```



Output video saved to `outputs/tracked.mp4`



\---



\## Configuration



All settings are in `configs/default.yaml`:

```yaml

model:

&#x20; weights: yolov8n.pt       # model size: n, s, m, l, x

&#x20; confidence: 0.3           # detection confidence threshold

&#x20; classes: \[2, 3, 5, 7]    # car, motorcycle, bus, truck



analytics:

&#x20; counting\_line:

&#x20;   start: \[0.1, 0.5]       # line position as fraction of frame

&#x20;   end: \[0.9, 0.5]

```



\---



\## Results



\- Processed 3000 frames of traffic footage

\- Counted 123 vehicles crossing the virtual line

\- Tracker maintained persistent IDs across full video duration

\- Pipeline runs at real-time capable speeds on CPU



\---



\## Tech stack



| Component | Tool |

|---|---|

| Object detection | YOLOv8n (Ultralytics) |

| Multi-object tracking | ByteTrack (BoxMOT) |

| Video processing | OpenCV |

| Config management | PyYAML |

| Testing | pytest |

| CI/CD | GitHub Actions |



\---



\## Key engineering decisions



\*\*Why ByteTrack?\*\* Simple, fast, no re-identification model needed. Works well on traffic scenes where objects follow predictable motion paths.



\*\*Why config-driven?\*\* Separating settings from code means changing the counting line or confidence threshold requires zero code changes — just edit the YAML.



\*\*Why YOLOv8n?\*\* The nano model is fast enough for real-time use on CPU while still achieving good detection accuracy on standard traffic scenes.



\---



\## Limitations



\- Tracking can lose IDs when vehicles are heavily occluded or overlap

\- Counting line is fixed per run — not adaptive to scene geometry

\- No re-identification — a vehicle that leaves and re-enters the frame gets a new ID

\- CPU inference is slower than real-time on high resolution video



\---



\## Author



Shiv Jayant Chaudhary

\[LinkedIn](https://linkedin.com/in/shiv1716) | \[GitHub](https://github.com/SHIVCHAUDHARY17)

