import unittest
import Part4


class TestHistogram(unittest.TestCase):
    def test1(self):
        data_list = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46,
                     52, 70, 99]
        self.assertEqual(Part4.histogram(data_list), [0, 5, 9, 8, 3, 1, 0, 1, 0, 1])

class TestHistogram(unittest.TestCase):
    def test1(self):
        Part4.print_histogram([0, 5, 9, 8, 3, 1, 0, 1, 0, 1])