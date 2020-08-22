import unittest
from bc.point import Point


class TestPoint(unittest.TestCase):
    def test_eq(self):
        p1 = Point(-1, -1, 5, 7)
        p2 = Point(-1, -1, 5, 7)
        self.assertEqual(p1, p2)

    def test_point_not_in_curve_raises_value_exception(self):
        with self.assertRaises(ValueError):
            p = Point(-1, -2, 5, 7)

    def test_add_additive_inverse(self):
        p1 = Point(None, None, 5, 7)
        p2 = Point(-1, -1, 5, 7)
        p3 = p1 + p2
        self.assertEqual(p3, p2)

        p1 = Point(-1, -1, 5, 7)
        p2 = Point(None, None, 5, 7)
        p3 = p1 + p2
        self.assertEqual(p3, p1)

    def test_add_tangent_point_zero_y(self):
        p1 = Point(-1, 0, 0, 1)
        p2 = Point(-1, 0, 0, 1)
        p3 = p1 + p2
        expected = Point(None, None, 0, 1)
        self.assertEqual(p3, expected)


if __name__ == "__main__":
    unittest.main()
