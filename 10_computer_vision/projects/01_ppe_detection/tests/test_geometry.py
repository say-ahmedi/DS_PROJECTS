import unittest

from ppe_detector.geometry import (
    horizontal_flip_xywhn,
    intersection_over_union,
    scale_xyxy,
    xywhn_to_xyxy,
)


class GeometryTests(unittest.TestCase):
    def test_iou_for_identical_disjoint_and_overlapping_boxes(self):
        box = (0, 0, 2, 2)
        self.assertEqual(intersection_over_union(box, box), 1.0)
        self.assertEqual(intersection_over_union(box, (3, 3, 4, 4)), 0.0)
        self.assertAlmostEqual(intersection_over_union(box, (1, 1, 3, 3)), 1 / 7)
        self.assertEqual(intersection_over_union(box, (2, 0, 4, 2)), 0.0)

    def test_normalized_box_and_flip(self):
        self.assertEqual(xywhn_to_xyxy(0.25, 0.5, 0.5, 1.0), (0, 0, 0.5, 1))
        self.assertEqual(horizontal_flip_xywhn(0.25, 0.5, 0.2, 0.4), (0.75, 0.5, 0.2, 0.4))
        with self.assertRaises(ValueError):
            horizontal_flip_xywhn(0.05, 0.5, 0.2, 0.4)

    def test_pixel_box_scaling(self):
        self.assertEqual(scale_xyxy((10, 20, 30, 40), (100, 100), (200, 50)), (20, 10, 60, 20))


if __name__ == "__main__":
    unittest.main()

