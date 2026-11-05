"""Make a small annotated contact sheet for manual label review."""

from __future__ import annotations

import random
from pathlib import Path

from PIL import Image, ImageDraw

from .dataset import CLASS_NAMES, images_in, label_path, read_labels
from .geometry import xywhn_to_xyxy


def make_contact_sheet(root: Path, output: Path, *, count: int = 10, seed: int = 20261104) -> list[str]:
    images = images_in(root.resolve(), "train")
    if count <= 0 or len(images) < count:
        raise ValueError("sample count must be positive and no greater than the training image count")
    chosen = random.Random(seed).sample(images, count)
    tile_width, tile_height = 480, 360
    columns = 2
    rows = (count + columns - 1) // columns
    sheet = Image.new("RGB", (columns * tile_width, rows * tile_height), "white")
    sheet_draw = ImageDraw.Draw(sheet)
    for index, path in enumerate(chosen):
        with Image.open(path) as source:
            image = source.convert("RGB")
        image.thumbnail((tile_width - 20, tile_height - 45), Image.Resampling.LANCZOS)
        draw = ImageDraw.Draw(image)
        for class_id, cx, cy, width, height in read_labels(label_path(root.resolve(), path)):
            x1, y1, x2, y2 = xywhn_to_xyxy(cx, cy, width, height)
            box = (x1 * image.width, y1 * image.height, x2 * image.width, y2 * image.height)
            name = CLASS_NAMES[class_id]
            color = "red" if name.startswith("no_") else ("blue" if name in {"Person", "forklift"} else "lime")
            draw.rectangle(box, outline=color, width=2)
            draw.text((box[0] + 2, max(0, box[1] - 12)), name, fill=color, stroke_width=1, stroke_fill="black")
        left = (index % columns) * tile_width + 10
        top = (index // columns) * tile_height + 25
        sheet.paste(image, (left, top))
        sheet_draw.text((left, top - 19), path.name, fill="black")
    output.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(output)
    return [str(path.relative_to(root.resolve())).replace("\\", "/") for path in chosen]
