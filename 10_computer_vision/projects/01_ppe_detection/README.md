# Worksite PPE Object Detection

Portfolio project A for the [Computer Vision roadmap](../../ROADMAP_2026_2027.md).

## Goal and current status

Detect people, protective equipment, and visible missing PPE in worksite images. The outcome is an evaluated, reproducible detector and a documented analysis of its mistakes. As of November 5, 2026, the [dataset audit](DATA_AUDIT_2026-11-05.md), frozen split, annotated contact sheet, audit/split/training commands, and geometry checks are complete. **No model training or accuracy result has been completed yet.**

The machine inspected for this project has an NVIDIA GeForce RTX 3050 Laptop GPU with **4 GB VRAM**, despite an earlier 8 GB estimate. Its system Python 3.14 environment has **CPU-only PyTorch 2.11**. Start with the small model, `imgsz=416`, `batch=2`; lower the batch to 1 if GPU memory is insufficient. Confirm a CUDA-enabled PyTorch install before training. The baseline settings are estimates, not benchmarked results.

## Dataset and evaluation policy

Use the [November 2026 Ultralytics Construction-PPE archive](https://docs.ultralytics.com/datasets/detect/construction-ppe). The current dataset card states 1,000 images, 12 classes, 800 published training images and 200 published validation images, with no separate test set. It describes both collected and generated imagery and a CC BY 4.0 data license. Attribute the Ultralytics team and record the archive version; the model/package license is separate.

For this portfolio project, the **published validation set is reserved as the final test set**. The `split` command partitions only the 800 published training images into approximately 680 train and 120 development images. It groups exact and close average-hash candidates before assignment and records the image lists and seed. The audit flags possible cross-split near duplicates for manual review. A hash match can be a false alarm; inspect flagged pairs before making claims about leakage. The 200-image final set is still from the same dataset sources, so it cannot establish performance on a live worksite.

Do not tune hyperparameters or thresholds against the reserved final set. Report class support, per-class AP, mAP50, mAP50–95, recall of missing-PPE classes, inference latency, and at least 30 inspected false positives or misses. Compare a baseline fine-tune with exactly one controlled change initially. A successful demonstration requires a clean setup, logged settings, runnable inference, and a limitations section, not a predetermined score.

## Setup

Use Python 3.12 if available. On this machine, a Python 3.12 interpreter exists at `C:\Users\Seidahmet\AppData\Roaming\uv\python\cpython-3.12.11-windows-x86_64-none\python.exe`. The project-local `.venv` has been created and the core package installed. From this directory in PowerShell:

```powershell
& 'C:\Users\Seidahmet\AppData\Roaming\uv\python\cpython-3.12.11-windows-x86_64-none\python.exe' -m venv .venv
.\.venv\Scripts\python.exe -m pip install -e .
```

For training, install a CUDA-enabled PyTorch build using the [official selector](https://pytorch.org/get-started/locally/), then install the project's training extra with `python -m pip install -e '.[train]'`. On this machine, PyTorch `2.14.1+cu126` and TorchVision `0.29.1+cu126` were installed from `https://download.pytorch.org/whl/cu126`. This shell initially sets `CUDA_VISIBLE_DEVICES=-1`, which hides the GPU. Set it to `0` for this PowerShell session and verify CUDA:

```powershell
$env:CUDA_VISIBLE_DEVICES = '0'
$env:YOLO_CONFIG_DIR = (Resolve-Path 'artifacts').Path
$env:MPLCONFIGDIR = (Resolve-Path 'artifacts').Path
.\.venv\Scripts\python.exe -c "import torch; print(torch.__version__, torch.cuda.is_available())"
```

The dataset archive can be downloaded using the link in the official dataset card. Extract it so that `data/construction-ppe/images/train` and `data/construction-ppe/labels/train` exist. The archive was downloaded and audited on this machine; its SHA-256 is in the [audit report](DATA_AUDIT_2026-11-05.md). Dataset files, model weights and generated runs stay outside Git.

## Commands

If using the system Python for the dependency-light checks, set the source path first:

```powershell
$env:PYTHONPATH = 'src'
python -m unittest discover -s tests -v
python -m ppe_detector audit data/construction-ppe --output artifacts/audit.json
python -m ppe_detector samples data/construction-ppe --output artifacts/annotated_samples.jpg
python -m ppe_detector split data/construction-ppe --output artifacts/split
```

After the train dependencies and CUDA are ready, use an official pretrained YOLO26n weight file. On this machine it was saved as ignored `weights/yolo26n.pt` from the [Ultralytics assets release](https://github.com/ultralytics/assets/releases/download/v8.4.0/yolo26n.pt) (SHA-256 `9b09cc8bf347f0fca5f7657480587f25db09b34bf33b0652110fb03a8ad4fef`). A missing named weight can also be downloaded automatically by Ultralytics where network access permits.

```powershell
.\.venv\Scripts\python.exe -m ppe_detector train --config artifacts/split/data.yaml --weights weights/yolo26n.pt --epochs 10 --image-size 416 --batch 2
.\.venv\Scripts\python.exe -m ppe_detector evaluate runs/<run-name>/weights/best.pt --config artifacts/split/data.yaml --split val
$devImage = Get-Content artifacts/split/val.txt -TotalCount 1
.\.venv\Scripts\python.exe -m ppe_detector predict runs/<run-name>/weights/best.pt $devImage
```

Only after selecting the model and analysis on the development set:

```powershell
.\.venv\Scripts\python.exe -m ppe_detector evaluate runs/<run-name>/weights/best.pt --config artifacts/split/data.yaml --split test --final-test --output artifacts/final_test.json
```

The CLI writes JSON reports under `artifacts/`. The [GPU smoke test](SMOKE_TEST_2026-11-05.md) used only 32 training and 8 development images for one epoch; its metrics are not a detector baseline. The service, Docker packaging, measured latency report, and model card are [scheduled milestones](../../ROADMAP_2026_2027.md), not completed components.

## Week 1 learning checks

- [x] Run the [dataset audit](DATA_AUDIT_2026-11-05.md) and explain class imbalance, rounded edge labels and duplicate candidates.
- [x] Inspect ten labeled images and write three observations.
- [x] Implement and test IoU for identical, disjoint, overlapping and edge-touching boxes.
- [ ] Work through the [hand calculation](math/01_boxes_iou.md) without reading the expected answer first.
- [x] Run pretrained inference and describe why generic pretrained detections are not PPE performance.
- [x] Make and review the frozen development split.
- [ ] Train and log one fine-tuning baseline.

