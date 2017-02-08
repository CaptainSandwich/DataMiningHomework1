import unittest
import Part2


class TestEqDepthMeans(unittest.TestCase):
    def test1(self):
        data_list = [4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34]
        self.assertEqual(Part2.equal_depth_means(data_list, 4), [[9.0, 9.0, 9.0, 9.0], [22.75, 22.75, 22.75, 22.75], [29.25, 29.25, 29.25, 29.25]])