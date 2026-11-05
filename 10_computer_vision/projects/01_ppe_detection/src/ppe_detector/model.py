"""Small, explicit wrappers around Ultralytics training and inference."""

from __future__ import annotations

import json
import time
from pathlib import Path


def _yolo():
    try:
        from ultralytics import YOLO
    except ImportError as exc:
        raise RuntimeError("install the project's train extra before training or inference") from exc
    return YOLO


def train(
    config: Path, runs_dir: Path, *, weights: str = "yolo26n.pt", epochs: int = 20,
    image_size: int = 416, batch: int = 2, allow_cpu: bool = False,
    run_prefix: str = "baseline",
) -> Path:
    if not config.is_file():
        raise FileNotFoundError(f"create the split before training: {config}")
    import torch

    has_gpu = torch.cuda.is_available()
    if not has_gpu and not allow_cpu:
        raise RuntimeError(
            "CUDA is unavailable. Install a CUDA-enabled PyTorch build, or pass --allow-cpu "
            "for a deliberately slow smoke run."
        )
    YOLO = _yolo()
    model = YOLO(weights)
    run_name = f"{run_prefix}_{int(time.time())}"
    model.train(
        data=str(config), epochs=epochs, imgsz=image_size, batch=batch,
        patience=5, workers=0, device=0 if has_gpu else "cpu", seed=20261104,
        project=str(runs_dir.resolve()), name=run_name, exist_ok=False,
    )
    return Path(model.trainer.save_dir)


def evaluate(weights: Path, config: Path, output: Path, *, split: str = "val", image_size: int = 416) -> dict:
    if split not in {"val", "test"}:
        raise ValueError("split must be val or test")
    if not weights.is_file() or not config.is_file():
        raise FileNotFoundError("weights and data.yaml must exist")
    YOLO = _yolo()
    result = YOLO(str(weights)).val(
        data=str(config), split=split, imgsz=image_size, workers=0,
        project=str((output.parent / "ultralytics_val").resolve()),
        name=output.stem, exist_ok=True,
    )
    box = result.box
    per_class = []
    for row in result.summary():
        per_class.append({
            "class": str(row["Class"]),
            "images": int(row["Images"]),
            "instances": int(row["Instances"]),
            "precision": float(row["Box-P"]),
            "recall": float(row["Box-R"]),
            "ap50": float(row["mAP50"]),
            "ap50_95": float(row["mAP50-95"]),
        })
    metrics = {
        "weights": str(weights.resolve()), "split": split, "image_size": image_size,
        "map50": float(box.map50), "map50_95": float(box.map),
        "mean_precision": float(box.mp), "mean_recall": float(box.mr),
        "per_class": per_class,
        "missing_ppe_classes": [row for row in per_class if row["class"].startswith("no_")],
        "speed_ms_per_image": {key: float(value) for key, value in result.speed.items()},
        "note": "Per-class metrics include only evaluated classes; do not interpret missing classes as zero AP.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(metrics, indent=2) + "\n", encoding="utf-8")
    return metrics


def predict(weights: Path, image: Path, output: Path, *, image_size: int = 416) -> dict:
    if not weights.is_file() or not image.is_file():
        raise FileNotFoundError("weights and input image must exist")
    YOLO = _yolo()
    prediction = YOLO(str(weights)).predict(source=str(image), imgsz=image_size, save=False, verbose=False)[0]
    detections = []
    for box in prediction.boxes:
        class_id = int(box.cls.item())
        detections.append({
            "class_id": class_id,
            "class_name": prediction.names[class_id],
            "confidence": float(box.conf.item()),
            "xyxy": [float(value) for value in box.xyxy[0].tolist()],
        })
    result = {"image": str(image.resolve()), "detections": detections}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    return result

