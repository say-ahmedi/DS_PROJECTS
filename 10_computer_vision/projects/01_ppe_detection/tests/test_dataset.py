import json
import random
import tempfile
import unittest
from pathlib import Path

from PIL import Image

from ppe_detector.dataset import audit_dataset, read_labels
from ppe_detector.split import create_split


def make_image(root: Path, split: str, name: str, seed: int) -> None:
    image_dir = root / "images" / split
    label_dir = root / "labels" / split
    image_dir.mkdir(parents=True, exist_ok=True)
    label_dir.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed)
    values = [rng.randrange(256) for _ in range(16 * 16)]
    image = Image.new("L", (16, 16))
    image.putdata(values)
    image.convert("RGB").save(image_dir / f"{name}.png")
    (label_dir / f"{name}.txt").write_text("0 0.5 0.5 0.25 0.25\n", encoding="utf-8")


class DatasetTests(unittest.TestCase):
    def test_audit_and_frozen_test_split(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp) / "construction-ppe"
            for index in range(8):
                make_image(root, "train", f"train{index}", index)
            make_image(root, "val", "published_val", 100)
            report = audit_dataset(root)
            self.assertEqual(report["images"], {"train": 8, "val": 1})
            self.assertEqual(report["class_counts"]["train"]["helmet"], 8)
            self.assertFalse(report["errors"])
            output = Path(temp) / "split"
            manifest = create_split(root, output, seed=42, dev_target=2)
            self.assertEqual(manifest["counts"]["test"], 1)
            self.assertEqual(manifest["counts"]["train"] + manifest["counts"]["val"], 8)
            self.assertEqual(manifest["images"]["test"], ["images/val/published_val.png"])
            self.assertEqual(json.loads((output / "data.yaml").read_text())["names"][0], "helmet")
            self.assertEqual(manifest["images"], create_split(root, output, seed=42, dev_target=2)["images"])

    def test_rejects_bad_yolo_box(self):
        with tempfile.TemporaryDirectory() as temp:
            label = Path(temp) / "invalid.txt"
            label.write_text("0 0.95 0.5 0.2 0.2\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "extends beyond"):
                list(read_labels(label))


if __name__ == "__main__":
    unittest.main()

