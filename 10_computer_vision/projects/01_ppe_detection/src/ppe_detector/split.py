"""Freeze a development split while reserving the supplied validation images."""

from __future__ import annotations

import json
import random
from pathlib import Path

from .dataset import CLASS_NAMES, audit_dataset, average_hash, images_in


def _groups(images: list[Path]) -> list[list[Path]]:
    """Keep exact and close average-hash candidates in the same partition."""
    hashes = [average_hash(path) for path in images]
    parent = list(range(len(images)))

    def find(index: int) -> int:
        while parent[index] != index:
            parent[index] = parent[parent[index]]
            index = parent[index]
        return index

    for i in range(len(images)):
        for j in range(i + 1, len(images)):
            if (hashes[i] ^ hashes[j]).bit_count() <= 2:
                parent[find(j)] = find(i)
    buckets: dict[int, list[Path]] = {}
    for index, image in enumerate(images):
        buckets.setdefault(find(index), []).append(image)
    return list(buckets.values())


def create_split(root: Path, output: Path, seed: int = 20261104, dev_target: int = 120) -> dict:
    root = root.resolve()
    report = audit_dataset(root)
    if report["errors"]:
        raise ValueError(f"dataset audit found {len(report['errors'])} errors; see the audit report")
    if any(item["kind"] == "exact" and len({name.split("/")[1] for name in item["images"]}) > 1
           for item in report["duplicate_candidates"]):
        raise ValueError("exact duplicate images cross the supplied train/validation boundary")
    train_images = images_in(root, "train")
    test_images = images_in(root, "val")
    groups = _groups(train_images)
    random.Random(seed).shuffle(groups)
    dev: list[Path] = []
    train: list[Path] = []
    for group in groups:
        if len(dev) < dev_target and len(dev) + len(group) <= dev_target + 10:
            dev.extend(group)
        else:
            train.extend(group)
    if not train or not dev:
        raise ValueError("unable to form non-empty training and development groups")
    output.mkdir(parents=True, exist_ok=True)
    split_paths = {"train": sorted(train), "val": sorted(dev), "test": sorted(test_images)}
    for name, paths in split_paths.items():
        (output / f"{name}.txt").write_text(
            "\n".join(path.as_posix() for path in paths) + "\n", encoding="utf-8"
        )
    manifest = {
        "dataset_root": str(root), "seed": seed,
        "policy": "aHash distance <= 2 grouped within supplied train; supplied val reserved as final test",
        "counts": {name: len(paths) for name, paths in split_paths.items()},
        "images": {
            name: [str(path.relative_to(root)).replace("\\", "/") for path in paths]
            for name, paths in split_paths.items()
        },
    }
    (output / "split_manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    config = {
        "train": (output / "train.txt").resolve().as_posix(),
        "val": (output / "val.txt").resolve().as_posix(),
        "test": (output / "test.txt").resolve().as_posix(),
        "names": list(CLASS_NAMES),
    }
    # JSON is a valid YAML subset and avoids a separate YAML dependency for data preparation.
    (output / "data.yaml").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    return manifest

