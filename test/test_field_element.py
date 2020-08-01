import unittest
from bc.field_element import FieldElement


class TestFieldElement(unittest.TestCase):
    def test_eq(self):
        a = FieldElement(10, 13)
        b = FieldElement(10, 13)
        self.assertEqual(a, b)

    def test_add(self):
        a = FieldElement(3, 13)
        b = FieldElement(7, 13)
        c = a + b
        expected = FieldElement(10, 13)
        self.assertEqual(c, expected)

    def test_sub(self):
        a = FieldElement(3, 13)
        b = FieldElement(7, 13)
        c = a - b
        expected = FieldElement(9, 13)
        self.assertEqual(c, expected)

    def test_mul(self):
        a = FieldElement(3, 13)
        b = FieldElement(7, 13)
        c = a * b
        expected = FieldElement(8, 13)
        self.assertEqual(c, expected)

    def test_div(self):
        a = FieldElement(3, 13)
        b = FieldElement(7, 13)
        c = a / b
        expected = FieldElement(5, 13)
        self.assertEqual(c, expected)

    def test_pow(self):
        a = FieldElement(3, 13)
        b = a ** 3
        expected = FieldElement(1, 13)
        self.assertEqual(b, expected)


if __name__ == "__main__":
    unittest.main()
