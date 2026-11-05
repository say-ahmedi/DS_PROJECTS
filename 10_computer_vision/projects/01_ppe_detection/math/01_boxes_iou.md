# Week 1 math exercise: image boxes and IoU

Given boxes `A = (0, 0, 2, 2)` and `B = (1, 1, 3, 3)` in `(x1, y1, x2, y2)` pixels:

1. Draw both boxes on graph paper.
2. Calculate each area, the intersection area, the union area, and IoU by hand.
3. Verify with `intersection_over_union` in `src/ppe_detector/geometry.py`.
4. Repeat for identical, disjoint, and edge-touching boxes. Explain why an edge-touch has IoU zero.
5. Convert normalized YOLO box `(cx=0.25, cy=0.5, w=0.2, h=0.4)` into corner coordinates. Flip the image horizontally and calculate the new center.

Expected check for the first pair: intersection `1`, union `7`, IoU `1/7`.

**Explain in your own words:** A detection is not correct merely because it names the right class. Its predicted box must overlap the annotated object sufficiently under the chosen IoU threshold.

