import unittest
import math

from shape2d.shape2d import Vector


class TestVector(unittest.TestCase):

    def test_create_from_numbers(self):
        v = Vector(1, 2)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)

    def test_create_from_list(self):
        v = Vector([1, 2])
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)

    def test_create_from_vector(self):
        v0 = Vector(1, 2)
        v = Vector(v0)
        self.assertEqual(v.x, 1)
        self.assertEqual(v.y, 2)

    def test_create_bad_sequence(self):
        with self.assertRaises(ValueError):
            v = Vector([1, 2, 3])
        with self.assertRaises(ValueError):
            v = Vector(1, 2, 3)

    def test_create_from_polar(self):
        v = Vector.polar(2, math.radians(30))
        self.assertAlmostEqual(v.x, 1.7320508075688774)
        self.assertAlmostEqual(v.y, 1)

        v = Vector.polar(3, -math.radians(45))
        self.assertAlmostEqual(v.x, 2.121320344)
        self.assertAlmostEqual(v.y, -2.121320344)



if __name__ == '__main__':
    unittest.main()
