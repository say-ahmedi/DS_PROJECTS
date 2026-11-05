"""Bounding-box operations used by the dataset checks and math exercises."""

from __future__ import annotations

import math
from typing import Sequence


def _box(values: Sequence[float]) -> tuple[float, float, float, float]:
    if len(values) != 4:
        raise ValueError("a box needs exactly four coordinates")
    box = tuple(float(value) for value in values)
    if not all(math.isfinite(value) for value in box):
        raise ValueError("box coordinates must be finite")
    x1, y1, x2, y2 = box
    if x2 < x1 or y2 < y1:
        raise ValueError("box corners are reversed")
    return box


def xywhn_to_xyxy(
    cx: float, cy: float, width: float, height: float
) -> tuple[float, float, float, float]:
    """Convert normalized YOLO center/size coordinates to corner coordinates."""
    values = (cx, cy, width, height)
    if not all(math.isfinite(value) for value in values):
        raise ValueError("box coordinates must be finite")
    if width <= 0 or height <= 0:
        raise ValueError("box width and height must be positive")
    return (cx - width / 2, cy - height / 2, cx + width / 2, cy + height / 2)


def intersection_over_union(a: Sequence[float], b: Sequence[float]) -> float:
    """Return IoU for two non-degenerate boxes in xyxy coordinates."""
    ax1, ay1, ax2, ay2 = _box(a)
    bx1, by1, bx2, by2 = _box(b)
    area_a = (ax2 - ax1) * (ay2 - ay1)
    area_b = (bx2 - bx1) * (by2 - by1)
    if area_a <= 0 or area_b <= 0:
        return 0.0
    intersection = max(0.0, min(ax2, bx2) - max(ax1, bx1)) * max(
        0.0, min(ay2, by2) - max(ay1, by1)
    )
    return intersection / (area_a + area_b - intersection)


def horizontal_flip_xywhn(
    cx: float, cy: float, width: float, height: float
) -> tuple[float, float, float, float]:
    """Flip a normalized YOLO box with its image around the vertical axis."""
    corners = xywhn_to_xyxy(cx, cy, width, height)
    if min(corners) < 0 or max(corners) > 1:
        raise ValueError("box must remain inside the normalized image")
    return (1 - cx, cy, width, height)


def scale_xyxy(
    box: Sequence[float], from_size: tuple[int, int], to_size: tuple[int, int]
) -> tuple[float, float, float, float]:
    """Scale pixel xyxy coordinates between (width, height) image sizes."""
    x1, y1, x2, y2 = _box(box)
    fw, fh = from_size
    tw, th = to_size
    if min(fw, fh, tw, th) <= 0:
        raise ValueError("image dimensions must be positive")
    return (x1 * tw / fw, y1 * th / fh, x2 * tw / fw, y2 * th / fh)

