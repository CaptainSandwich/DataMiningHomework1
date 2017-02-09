import unittest
import Part1


class TestGetData(unittest.TestCase):
    def test_1(self):
        data = Part1.get_data('TestData/Part1/test_set1')
        self.assertEqual(data, [0, 1, 2])

    def test_2(self):
        self.assertEqual(Part1.get_data('TestData/Part1/test_set2'),
                         [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40,
                          45, 46, 52, 70])

    def test_3(self):
        self.assertEqual(Part1.get_data('TestData/Part1/test_set3'), [0])

    def test_nonexistent(self):
        self.assertRaises(IOError, Part1.get_data('TestData/Part1/test_bogus'))

    def test_empty(self):
        self.assertIsNone(Part1.get_data('TestData/Part1/test_empty'))


class TestGetMean(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(Part1.get_mean([0, 1, 2]), 1, 4)

    def test_2(self):
        self.assertAlmostEqual(Part1.get_mean(
            [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52,
             70]), 29.963, 4)

    def test_3(self):
        self.assertAlmostEqual(Part1.get_mean([0]), 0, 4)

    def test_empty(self):
        self.assertRaises(TypeError, Part1.get_mean([]))


class TestGetMidrange(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(Part1.get_midrange([0, 1, 2]), 1, 4)

    def test_2(self):
        self.assertAlmostEqual(Part1.get_midrange(
            [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52,
             70]), 41.5, 4)

    def test_empty(self):
        self.assertRaises(ValueError, Part1.get_midrange([]))


class TestGetMedian(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Part1.get_median([0, 1, 2]), 1)

    def test_2(self):
        self.assertEqual(Part1.get_median(
            [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52,
             70]), 25, 4)

    def test_3(self):
        self.assertAlmostEqual(Part1.get_median([0, 1, 2, 3]), 1.5, 4)

    def test_4(self):
        self.assertAlmostEqual(Part1.get_median([4, 5, 6, 7]), 5.5, 4)

    def test_5(self):
        self.assertAlmostEqual(Part1.get_median([5]), 5, 4)


class TestGetQ1(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(Part1.get_q1([0, 1, 2]), 0, 4)

    def test_2(self):
        self.assertEqual(Part1.get_q1(
            [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52,
             70]), 20, 4)

    def test_3(self):
        self.assertAlmostEqual(Part1.get_q1([0, 1, 2, 3]), 0.5, 4)

    def test_4(self):
        self.assertAlmostEqual(Part1.get_q1([4, 5, 6, 7]), 4.5, 4)

    def test_5(self):
        self.assertAlmostEqual(Part1.get_q1([3, 5, 7, 8, 12, 13, 14, 18, 21]), 6, 4)

    def test_6(self):
        self.assertAlmostEqual(Part1.get_q1([5, 6, 7]), 5, 4)


class TestGetQ3(unittest.TestCase):
    def test_1(self):
        self.assertAlmostEqual(Part1.get_q3([0, 1, 2]), 2, 4)

    def test_2(self):
        self.assertEqual(Part1.get_q3(
            [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52,
             70]), 35, 4)

    def test_3(self):
        self.assertAlmostEqual(Part1.get_q3([0, 1, 2, 3]), 2.5, 4)

    def test_4(self):
        self.assertAlmostEqual(Part1.get_q3([4, 5, 6, 7]), 6.5, 4)

    def test_5(self):
        self.assertAlmostEqual(Part1.get_q3([3, 5, 7, 8, 12, 13, 14, 18, 21]), 16, 4)

    def test_6(self):
        self.assertAlmostEqual(Part1.get_q3([5, 6, 7]), 7, 4)


class TestGetMode(unittest.TestCase):
    def test_1(self):
        self.assertEqual(Part1.get_mode([0, 1, 1]), ["unimodal", [1]])

    def test_2(self):
        self.assertEqual(Part1.get_mode([0, 1, 1, 2, 2]), ["bimodal", [1, 2]])

    def test_3(self):
        self.assertEqual(Part1.get_mode([0, 1, 1, 2, 2, 3, 3]), ["trimodal", [1, 2, 3]])

    def test_4(self):
        self.assertEqual(Part1.get_mode([0, 1, 1, 2, 2, 3, 3, 4, 4]), ["multimodal", [1, 2, 3, 4]])

    def test_5(self):
        self.assertEqual(Part1.get_mode([0, 1, 2, 4, 1, 3, 2, 3, 4]), ["multimodal", [1, 2, 3, 4]])

def main():
    unittest.main(buffer=True)


if __name__ == '__main__':
    main()
