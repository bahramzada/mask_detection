# Mask Detection

This repository contains code and resources for building a mask detection system using deep learning and real-time computer vision. The goal is to detect whether people in images or video streams (e.g., from a camera) are wearing masks, leveraging object detection models and labeled datasets.

## Dataset

We use the [YOLO Labeled Mask Detection Dataset](https://www.kaggle.com/datasets/raullte/yolo-labeled-mask-detection-dataset) from Kaggle. This dataset contains images annotated for mask detection with YOLO format labels, making it suitable for training object detection models.

- **Dataset Link:** [Kaggle: YOLO-Labeled Mask Detection Dataset](https://www.kaggle.com/datasets/raullte/yolo-labeled-mask-detection-dataset)

## Features

- Mask detection using deep learning (YOLO supported)
- Dataset preparation and visualization scripts
- Training and evaluation scripts
- **Real-time mask detection using cv2 (OpenCV) and camera input**
- Inference/demo code for images and live video streams

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bahramzada/mask_detection.git
cd mask_detection
```

### 2. Download the Dataset

Download the dataset from [Kaggle](https://www.kaggle.com/datasets/raullte/yolo-labeled-mask-detection-dataset) and place it in a suitable folder (e.g., `data/`).

### 3. Install Dependencies

Make sure you have Python 3.x installed. Then install the required packages:

```bash
pip install -r requirements.txt
```

### 4. Training

Refer to the training scripts (e.g., `train.py`) in the repository to train your mask detection model. Configure the dataset path and other hyperparameters as needed.

### 5. Real-Time Camera Object Detection

Use the provided scripts (e.g., `camera_detect.py` or similar) to perform real-time mask detection using your camera. This utilizes OpenCV (`cv2`) for capturing video frames and running object detection on each frame.

Example usage:

```bash
python camera_detect.py
```

This will open your default camera and display live detection results.

### 6. Inference/Demo

You can also run mask detection on static images or video files using the inference scripts (e.g., `detect.py`).

## Folder Structure

```
mask_detection/
├── data/                # Place your downloaded dataset here
├── models/              # Model weights and architecture files
├── scripts/             # Utility scripts
├── train.py             # Training script
├── detect.py            # Inference script (images/videos)
├── camera_detect.py     # Real-time camera object detection
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Citation

If you use this dataset or code, please cite the original dataset and this repository.

## License

This project is licensed under the MIT License.

---

**Dataset Credit:** [raullte on Kaggle](https://www.kaggle.com/raullte)
