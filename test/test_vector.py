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

    def test_iter(self):
        v = Vector(10, 20)
        l = list(v)
        self.assertEqual(l, [10, 20])
        t = (10, 20)
        for a, b in zip(l, t):
            self.assertEqual(a, b)

    def test_len(self):
        v = Vector(0, 0)
        self.assertEqual(len(v), 2)

    def test_get_item(self):
        v = Vector(10, 20)
        self.assertEqual(v[0], 10)
        self.assertEqual(v[1], 20)
        self.assertEqual(v[-1], 20)
        self.assertEqual(v[-2], 10)
        with self.assertRaises(IndexError):
            v[2]
        with self.assertRaises(IndexError):
            v[-3]

    def test_get_item(self):
        v1 = Vector(10, 20)
        v2 = Vector(10, 20)
        v3 = Vector(1, 2)
        eq1 = v1 == v2
        eq2 = v1 == v3
        self.assertEqual(eq1, True)
        self.assertEqual(eq2, False)

    def test_neg(self):
        v1 = Vector(10, 20)
        v2 = -v1
        self.assertEqual(v2, Vector(-10, -20))
    def test_add(self):
        v1 = Vector(10, 20)
        v2 = Vector(1, 2)
        v3 = v1 + v2
        self.assertEqual(v3, Vector(11, 22))

    def test_sub(self):
        v1 = Vector(10, 20)
        v2 = Vector(1, 2)
        v3 = v1 - v2
        self.assertEqual(v3, Vector(9, 18))

    def test_mul(self):
        v1 = Vector(10, 20)
        v2 = v1 * 2
        self.assertEqual(v2, Vector(20, 40))
        v2 = -3 * v1
        self.assertEqual(v2, Vector(-30, -60))

    def test_div(self):
        v1 = Vector(10, 20)
        v2 = v1 / 2
        self.assertEqual(v2, Vector(5, 10))
        v2 = v1 // 3
        self.assertEqual(v2, Vector(3, 6))

    def test_length(self):
        v = Vector(10, 20)
        self.assertAlmostEqual(v.length, 22.360679775)

    def test_angle(self):
        v = Vector(10, 20)
        self.assertAlmostEqual(v.angle, 1.10714871779)

    def test_unit(self):
        v = Vector(10, 20)
        u = v.unit
        self.assertAlmostEqual(u.x, 10/math.sqrt(500))
        self.assertAlmostEqual(u.y, 20/math.sqrt(500))

    def test_str(self):
        v = Vector(2, 5)
        s = str(v)
        self.assertEqual(s, "Vector(2.000, 5.000)")

    def test_repr(self):
        v = Vector(math.sqrt(2), math.sqrt(5))
        s = repr(v)
        self.assertEqual(s, "Vector(1.4142135623730951, 2.23606797749979)")


if __name__ == '__main__':
    unittest.main()
