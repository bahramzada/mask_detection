# Mask Detection

This repository contains code and resources for building a mask detection system using deep learning. The goal is to detect whether people in images are wearing masks or not, leveraging computer vision models and labeled datasets.

## Dataset

We use the [YOLO Labeled Mask Detection Dataset](https://www.kaggle.com/datasets/raullte/yolo-labeled-mask-detection-dataset) from Kaggle. This dataset contains images annotated for mask detection with YOLO format labels, making it suitable for training object detection models.

- **Dataset Link:** [Kaggle: YOLO-Labeled Mask Detection Dataset](https://www.kaggle.com/datasets/raullte/yolo-labeled-mask-detection-dataset)

## Features

- Mask detection using deep learning (YOLO supported)
- Dataset preparation and visualization scripts
- Training and evaluation scripts
- Inference/demo code for real-time mask detection

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

### 5. Inference/Demo

Use the inference scripts (e.g., `detect.py`) to run mask detection on new images or video streams.

## Folder Structure

```
mask_detection/
├── data/                # Place your downloaded dataset here
├── models/              # Model weights and architecture files
├── scripts/             # Utility scripts
├── train.py             # Training script
├── detect.py            # Inference script
├── requirements.txt     # Python dependencies
└── README.md            # This file
```

## Citation

If you use this dataset or code, please cite the original dataset and this repository.

## License

This project is licensed under the MIT License.

---

**Dataset Credit:** [raullte on Kaggle](https://www.kaggle.com/raullte)
