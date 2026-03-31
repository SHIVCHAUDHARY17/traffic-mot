\# 🚗 Traffic Multi-Object Tracking



> Real-time vehicle detection, tracking, and counting in traffic video using \*\*YOLOv8\*\* and \*\*ByteTrack\*\*.



!\[CI](https://github.com/SHIVCHAUDHARY17/traffic-mot/actions/workflows/ci.yml/badge.svg)

!\[Python](https://img.shields.io/badge/python-3.11-blue)

!\[License](https://img.shields.io/badge/license-MIT-green)



\---



\## 📌 Overview



This project extends single-frame object detection into \*\*video-based dynamic perception\*\* — a core requirement in autonomous driving and intelligent transport systems.



Given a traffic video, the pipeline:

\- \*\*Detects\*\* vehicles frame-by-frame using YOLOv8

\- \*\*Tracks\*\* each vehicle across frames with a persistent ID using ByteTrack

\- \*\*Counts\*\* vehicles crossing a configurable virtual line

\- \*\*Outputs\*\* a fully annotated video with bounding boxes, class labels, track IDs, and live count



\---



\## 🔁 Pipeline Architecture



!\[Pipeline](docs/pipeline.png)

```

Traffic Video → Frame Reader → YOLO Detector → ByteTrack → Line Counter → Annotator → Output Video

```



\---



\## 🎬 Input / Output



| Input Frame | Output Frame |

|---|---|

| !\[Input](docs/input\_frame.jpg) | !\[Output](docs/output\_frame.jpg) |



> Output frame at timestep 1550 — 14 vehicles tracked simultaneously with unique IDs and count overlay



\---



\## 📁 Project Structure

```

traffic-mot/

├── src/

│   ├── detector.py        # YOLOv8 wrapper — per-frame detection

│   ├── tracker.py         # ByteTrack wrapper — persistent track IDs

│   ├── analytics.py       # Virtual line crossing counter

│   ├── annotator.py       # Draws boxes, IDs, count on each frame

│   └── pipeline.py        # End-to-end orchestrator

├── configs/

│   └── default.yaml       # All settings — model, thresholds, line position

├── tests/

│   └── test\_analytics.py  # pytest unit tests for counting logic

├── .github/workflows/

│   └── ci.yml             # GitHub Actions CI — runs tests on every push

├── docs/                  # Pipeline diagram and demo frames

└── run\_tracker.py         # CLI entry point

```



\---



\## ⚙️ Setup

```bash

git clone https://github.com/SHIVCHAUDHARY17/traffic-mot.git

cd traffic-mot

python -m venv venv

venv\\Scripts\\activate        # Linux/Mac: source venv/bin/activate

pip install -r requirements.txt

```



\---



\## 🚀 Usage



Place your traffic video at `data/sample.mp4` and run:

```bash

python run\_tracker.py --config configs/default.yaml

```



Annotated output saved to `outputs/tracked.mp4`



\---



\## 🛠️ Configuration



All settings live in `configs/default.yaml` — no code changes needed:

```yaml

model:

&#x20; weights: yolov8n.pt     # swap to yolov8s.pt or yolov8m.pt for more accuracy

&#x20; confidence: 0.3         # lower = more detections, higher = fewer false positives

&#x20; classes: \[2, 3, 5, 7]  # COCO IDs: car, motorcycle, bus, truck



analytics:

&#x20; counting\_line:

&#x20;   start: \[0.1, 0.5]     # line position as fraction of frame size

&#x20;   end: \[0.9, 0.5]       # 0.5 = horizontal line at vertical midpoint

```



\---



\## 📊 Results



| Metric | Value |

|---|---|

| Video length | 3000 frames |

| Vehicles counted | 123 |

| Max vehicles tracked simultaneously | 14 |

| Detection classes | Car, Motorcycle, Bus, Truck |

| Model used | YOLOv8n (nano) |



\---



\## 🧪 Testing and CI

```bash

py -m pytest tests/ -v

```



5 unit tests covering counting logic — no crossing, single crossing, double-count prevention, multiple vehicles, above-line filtering.



GitHub Actions runs all tests automatically on every push. Green badge = all passing.



\---



\## 🧰 Tech Stack



| Component | Tool |

|---|---|

| Object detection | YOLOv8n (Ultralytics) |

| Multi-object tracking | ByteTrack (BoxMOT) |

| Video processing | OpenCV |

| Config management | PyYAML |

| Testing | pytest |

| CI/CD | GitHub Actions |



\---



\## ⚠️ Limitations



\- Track IDs reset if a vehicle leaves and re-enters the frame

\- Counting line is fixed per run — not adaptive

\- CPU inference is slower than real-time on 1080p+ video

\- Occlusion between vehicles can cause brief ID switches



\---



\## 👤 Author



\*\*Shiv Jayant Chaudhary\*\*

Computer Vision and Machine Learning Engineer



\[!\[LinkedIn](https://img.shields.io/badge/LinkedIn-shiv1716-blue)](https://linkedin.com/in/shiv1716)

\[!\[GitHub](https://img.shields.io/badge/GitHub-SHIVCHAUDHARY17-black)](https://github.com/SHIVCHAUDHARY17)

