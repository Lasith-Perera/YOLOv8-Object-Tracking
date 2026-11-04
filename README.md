# YOLOv8 Object Tracking

A Python-based object detection and tracking project using **Ultralytics YOLOv8** and **OpenCV**. It processes a video, detects objects frame by frame, and displays annotated frames in a live window.

![YOLOv8 Object Tracking Demo](Yolov8%20Object%20Tracking.jpeg)
## Features

- Detects objects in a video using the pretrained YOLOv8 Nano model (`yolov8n.pt`).
- Tracks detected objects across consecutive frames using `model.track(..., persist=True)`.
- Displays detection boxes, class labels, and tracking annotations provided by Ultralytics.
- Stops automatically when the video ends or when the user presses **Q**.
- Checks that the input video can be opened before processing.

## Technologies

- Python
- [Ultralytics YOLOv8](https://docs.ultralytics.com/)
- [OpenCV](https://opencv.org/)
- `lap` (tracking dependency)

## Project Structure

```text
Yolov8 Object Tracking/
├── main.py           # Video detection and tracking
├── test.mp4          # Input video (provide locally)
├── yolov8n.pt        # Pretrained model (downloaded automatically if absent)
├── README.md
└── .gitignore
```

> The video, model weights, and virtual environment may be excluded from Git using `.gitignore`.

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

Replace the placeholders with your GitHub repository details.

### 2. Create a virtual environment

On Windows (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell prevents activation, you can run the virtual environment's Python directly: `\.venv\Scripts\python.exe` (from the project directory).

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install ultralytics opencv-python "lap>=0.5.12"
```

### 4. Add the input video

Place a video named `test.mp4` in the project root, or update the `video_path` variable in `main.py` to point to your file.

### 5. Run the project

```bash
python main.py
```

The application opens an OpenCV window showing annotated video frames. Press **Q** to stop tracking.

## How It Works

1. Load the pretrained YOLOv8 Nano model.
2. Open the input video with OpenCV.
3. Read one frame at a time until the video ends.
4. Use `model.track(frame, persist=True)` to detect and track objects across frames.
5. Draw Ultralytics annotations with `results[0].plot()` and display the resulting frame.
6. Release the video and close OpenCV windows after processing.

## Troubleshooting

| Issue | Solution |
| --- | --- |
| `No module named 'ultralytics'` | Install dependencies in the Python environment used to run the project. |
| `lap>=0.5.12` missing | Run `python -m pip install "lap>=0.5.12"`. |
| `Could not open video` | Check that `test.mp4` exists or update `video_path`. |
| Video window does not appear | Run the program in a desktop environment with GUI support and ensure `opencv-python` is installed. |
| Model file missing | Ultralytics typically downloads `yolov8n.pt` on first use when internet access is available. |

## Notes

- Performance depends on the video resolution and available CPU/GPU hardware.
- This demo displays annotated video; it does **not** save an output video file.
- Only process videos that you have permission to use.

## Data

You can download the video I used in this project [here](https://drive.google.com/file/d/1TM3KF_JC_j9znTjtsGxF8InmUbPPPOUE/view?usp=sharing).

## Acknowledgements

Built using [Ultralytics YOLO](https://docs.ultralytics.com/) and [OpenCV](https://opencv.org/).
