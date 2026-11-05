"""Audit the November 2026 Construction-PPE YOLO image/label archive."""

from __future__ import annotations

from collections import Counter, defaultdict
from hashlib import sha256
from pathlib import Path
from typing import Iterator

from PIL import Image, UnidentifiedImageError
import numpy as np

from .geometry import xywhn_to_xyxy

CLASS_NAMES = (
    "helmet", "gloves", "vest", "boots", "goggles", "Person",
    "no_helmet", "no_goggle", "no_gloves", "no_boots", "forklift", "no_vest",
)
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".bmp", ".webp"}


def images_in(root: Path, split: str) -> list[Path]:
    folder = root / "images" / split
    if not folder.is_dir():
        raise FileNotFoundError(f"missing image directory: {folder}")
    return sorted(path for path in folder.rglob("*") if path.suffix.lower() in IMAGE_SUFFIXES)


def label_path(root: Path, image: Path) -> Path:
    relative = image.relative_to(root / "images")
    return (root / "labels" / relative).with_suffix(".txt")


def read_labels(path: Path) -> Iterator[tuple[int, float, float, float, float]]:
    if not path.is_file():
        raise FileNotFoundError(f"missing label file: {path}")
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        fields = line.split()
        if len(fields) != 5:
            raise ValueError(f"{path}:{line_number}: expected class, cx, cy, width, height")
        try:
            class_id = int(fields[0])
            cx, cy, width, height = (float(value) for value in fields[1:])
        except ValueError as exc:
            raise ValueError(f"{path}:{line_number}: invalid label value") from exc
        if not 0 <= class_id < len(CLASS_NAMES):
            raise ValueError(f"{path}:{line_number}: class {class_id} is outside 0–11")
        x1, y1, x2, y2 = xywhn_to_xyxy(cx, cy, width, height)
        # The archive rounds coordinates to six decimals; boxes on the edge can
        # extend by 0.000005 after conversion back to corners.
        if min(x1, y1) < -1e-5 or max(x2, y2) > 1 + 1e-5:
            raise ValueError(f"{path}:{line_number}: box extends beyond normalized image")
        yield (class_id, cx, cy, width, height)


def average_hash(path: Path) -> int:
    """A cheap near-duplicate candidate hash; every match still needs inspection."""
    with Image.open(path) as image:
        pixels = np.asarray(image.convert("L").resize((8, 8), Image.Resampling.LANCZOS)).ravel()
    mean = float(pixels.mean())
    return sum((pixel > mean) << index for index, pixel in enumerate(pixels))


def audit_dataset(root: Path) -> dict:
    root = root.resolve()
    result: dict = {
        "dataset_root": str(root),
        "source": "https://docs.ultralytics.com/datasets/detect/construction-ppe",
        "expected_version": "November 2026; 12 classes; 800 train / 200 validation",
        "images": {}, "boxes": {}, "class_counts": {}, "sizes": {},
        "rounding_edge_boxes": 0,
        "errors": [], "warnings": [], "duplicate_candidates": [],
    }
    hashes: dict[str, list[tuple[str, str]]] = defaultdict(list)
    perceptual: list[tuple[str, str, int]] = []
    counts = Counter()
    for split in ("train", "val"):
        images = images_in(root, split)
        result["images"][split] = len(images)
        result["boxes"][split] = 0
        sizes = Counter()
        for image in images:
            relative = str(image.relative_to(root)).replace("\\", "/")
            try:
                with Image.open(image) as opened:
                    sizes[f"{opened.width}x{opened.height}"] += 1
                    opened.verify()
                label_count = 0
                for class_id, cx, cy, width, height in read_labels(label_path(root, image)):
                    counts[(split, CLASS_NAMES[class_id])] += 1
                    label_count += 1
                    x1, y1, x2, y2 = xywhn_to_xyxy(cx, cy, width, height)
                    if min(x1, y1) < 0 or max(x2, y2) > 1:
                        result["rounding_edge_boxes"] += 1
                result["boxes"][split] += label_count
                hashes[sha256(image.read_bytes()).hexdigest()].append((split, relative))
                perceptual.append((split, relative, average_hash(image)))
            except (OSError, ValueError, UnidentifiedImageError) as exc:
                result["errors"].append(f"{relative}: {exc}")
        result["sizes"][split] = dict(sizes.most_common())
    result["class_counts"] = {
        split: {name: counts[(split, name)] for name in CLASS_NAMES}
        for split in ("train", "val")
    }
    for matches in hashes.values():
        if len(matches) > 1:
            result["duplicate_candidates"].append(
                {"kind": "exact", "images": [name for _, name in matches]}
            )
    # Inspect cross-split near matches first; aHash can flag visually similar scenes.
    train_hashes = [(name, value) for split, name, value in perceptual if split == "train"]
    val_hashes = [(name, value) for split, name, value in perceptual if split == "val"]
    for train_name, train_hash in train_hashes:
        for val_name, val_hash in val_hashes:
            distance = (train_hash ^ val_hash).bit_count()
            if distance <= 2:
                result["duplicate_candidates"].append(
                    {"kind": "near_cross_split", "images": [train_name, val_name], "distance": distance}
                )
                if len(result["duplicate_candidates"]) >= 100:
                    break
        if len(result["duplicate_candidates"]) >= 100:
            break
    if result["images"] != {"train": 800, "val": 200}:
        result["warnings"].append("image counts differ from the November 2026 dataset card; verify the archive version")
    if result["errors"]:
        result["warnings"].append("fix invalid images or labels before making a split or training")
    if result["rounding_edge_boxes"]:
        result["warnings"].append(
            "some edge boxes exceed normalized bounds by at most 0.00001 due to label rounding"
        )
    if result["duplicate_candidates"]:
        result["warnings"].append("inspect duplicate candidates manually; average-hash matches are not proof of duplication")
    return result

