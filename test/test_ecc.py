import unittest
from bc.field_element import FieldElement
from bc.point import Point


class TestEcc(unittest.TestCase):
    prime = 223
    a = FieldElement(0, prime)
    b = FieldElement(7, prime)

    def test_on_curve(self):
        valid_points = ((192, 105), (17, 56), (1, 193))
        for x_raw, y_raw in valid_points:
            x = FieldElement(x_raw, self.prime)
            y = FieldElement(y_raw, self.prime)
            p = Point(x, y, self.a, self.b)
            self.assertIsInstance(p, Point)

    def test_not_on_curve(self):
        invalid_points = ((200, 119), (42, 99))
        for x_raw, y_raw in invalid_points:
            x = FieldElement(x_raw, self.prime)
            y = FieldElement(y_raw, self.prime)
            with self.assertRaises(ValueError):
                p = Point(x, y, self.a, self.b)

    def test_add_same_point(self):
        prime = 223
        a = FieldElement(num=0, prime=prime)
        b = FieldElement(num=7, prime=prime)
        x1 = FieldElement(192, prime=prime)
        y1 = FieldElement(105, prime=prime)

        x_expected = FieldElement(49, prime=prime)
        y_expected = FieldElement(71, prime=prime)
        p_expected = Point(x_expected, y_expected, a, b)
        # 49, 71
        p1 = Point(x1, y1, a, b)

        self.assertEqual(p1 + p1, p_expected)

    def test_add(self):
        prime = 223
        a = FieldElement(num=0, prime=prime)
        b = FieldElement(num=7, prime=prime)

        additions = (
            # (x1, y1, x2, y2, x3, y3)
            (192, 105, 17, 56, 170, 142),
            (47, 71, 117, 141, 60, 139),
            (143, 98, 76, 66, 47, 71),
        )

        for addition in additions:
            _x1, _y1, _x2, _y2, _x3, _y3 = addition
            x1 = FieldElement(_x1, prime)
            y1 = FieldElement(_y1, prime)
            x2 = FieldElement(_x2, prime)
            y2 = FieldElement(_y2, prime)
            x3 = FieldElement(_x3, prime)
            y3 = FieldElement(_y3, prime)

            p1 = Point(x1, y1, a, b)
            p2 = Point(x2, y2, a, b)
            p3 = Point(x3, y3, a, b)

            self.assertEqual(p1 + p2, p3)

    def test_rmul(self):
        # tests the following scalar multiplications
        # 2*(192,105)
        # 2*(143,98)
        # 2*(47,71)
        # 4*(47,71)
        # 8*(47,71)
        # 21*(47,71)
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        multiplications = (
            # (coefficient, x1, y1, x2, y2)
            (2, 192, 105, 49, 71),
            (2, 143, 98, 64, 168),
            (2, 47, 71, 36, 111),
            (4, 47, 71, 194, 51),
            (8, 47, 71, 116, 55),
            (21, 47, 71, None, None),
        )

        for s, x1_raw, y1_raw, x2_raw, y2_raw in multiplications:
            x1 = FieldElement(x1_raw, prime)
            y1 = FieldElement(y1_raw, prime)
            p1 = Point(x1, y1, a, b)
            # initialize the second point based on whether it's the point at infinity
            if x2_raw is None:
                p2 = Point(None, None, a, b)
            else:
                x2 = FieldElement(x2_raw, prime)
                y2 = FieldElement(y2_raw, prime)
                p2 = Point(x2, y2, a, b)

            # check that the product is equal to the expected point
            self.assertEqual(s * p1, p2)


if __name__ == "__main__":
    unittest.main()
