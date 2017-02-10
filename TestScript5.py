import Part5
import unittest


class TestGetData(unittest.TestCase):
    def test1(self):
        data_list = Part5.get_file_data("Points")
        self.assertEqual(data_list, [[5, 2], [1.5, 1.7], [2.0, 1.9], [1.6, 1.8],
                                     [1.2, 1.5], [1.5, 1.0]])


class TestGetCovariance(unittest.TestCase):
    def test1(self):
        data_list = [[2,5],[3,8],[5,10],[4,11],[6,14]]
        self.assertAlmostEqual(Part5.covariance(data_list, 0, 1), 4)
