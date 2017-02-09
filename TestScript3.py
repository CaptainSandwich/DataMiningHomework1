import unittest
import Part3


class TestMinMax(unittest.TestCase):
    def test1(self):
        self.assertEqual(Part3.min_max([0, 50, 100], 0, 1), [0, 0.5, 1])

    def test2(self):
        data_list = Part3.min_max([12000, 73600, 98000], 0, 1)
        self.assertEqual(data_list[0], 0)
        self.assertAlmostEqual(data_list[1], 0.716, 3)
        self.assertEqual(data_list[2], 1)


class TestZScore(unittest.TestCase):
    def test1(self):
        self.assertEqual(Part3.z_score([0, 1, 2, 3, 4, 5, 6]), [-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])


class TestDecimalScaling(unittest.TestCase):
    def test1(self):
        self.assertEqual(Part3.decimal_scaling([-918, -800, -700, 200, 300, 900]), [-0.918, -0.8, -0.7, 0.2, 0.3, 0.9])
