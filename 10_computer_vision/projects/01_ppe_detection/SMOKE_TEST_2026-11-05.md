# GPU pipeline smoke test — November 5, 2026

This is a **software check**, not a portfolio baseline or a detector-quality estimate. It used 32 images from the frozen training split and 8 images from the development split, with YOLO26n pretrained COCO weights, one epoch, 320-pixel input, batch size 1, and the local RTX 3050 Laptop GPU (4 GB VRAM). It did not touch the reserved 200-image final test set.

The train and evaluation commands completed with Ultralytics 8.4.202, PyTorch 2.14.1+cu126 and Python 3.12.11. The machine's shell sets `CUDA_VISIBLE_DEVICES=-1`; overriding it to `0` exposed the GPU. The smoke run's output is ignored by Git under `runs/` and `artifacts/`.

On the eight-image sample, mAP50 was **0.0474**, mAP50–95 was **0.0270**, and missing-PPE recall was **zero**. These numbers are unstable because the sample is tiny and training lasted only one epoch. Some classes had no instances in those eight images. The next meaningful result must come from training on all 680 training images and evaluating on the 120-image development set.

Generic pretrained inference on one PPE image produced `person` and `truck` detections. Those are COCO categories, not any of the 12 fine-tuned PPE classes, and they are not a PPE score.
