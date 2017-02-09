import unittest
import Part2


class TestEqDepthMeans(unittest.TestCase):
    def test1(self):
        data_list = [4, 8, 9, 15, 21, 21, 24, 25, 26, 28, 29, 34]
        self.assertEqual(Part2.equal_depth_means(data_list, 4), [[9.0, 9.0, 9.0, 9.0], [22.75, 22.75, 22.75, 22.75], [29.25, 29.25, 29.25, 29.25]])

    def test2(self):
        data_list = [4, 8, 15, 21, 21, 24, 25, 28, 34]
        self.assertEqual(Part2.equal_depth_means(data_list, 3), [[9, 9, 9], [22, 22, 22], [29, 29, 29]])

    def test3(self):
        data_list = [4, 8, 15, 21, 21, 24, 25, 28, 34]
        self.assertEqual(Part2.equal_depth_means(data_list, 2), [[6, 6], [18, 18], [22.5, 22.5], [26.5, 26.5], [34]])


class TestEqDepthBoundaries(unittest.TestCase):
    def test1(self):
        data_list = [4, 8, 15, 21, 21, 24, 25, 28, 34]
        self.assertEqual(Part2.equal_depth_boundaries(data_list, 3), [[4, 4, 15], [21, 21, 24], [25, 25, 34]])

    def test2(self):
        data_list = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
        self.assertEqual(Part2.equal_depth_boundaries(data_list, 3), [[13, 16, 16], [16, 20, 20], [20, 22, 22], [22, 25, 25], [25, 25, 30], [33, 33, 35], [35, 35, 35], [36, 36, 45], [46, 46, 70]])

    def test3(self):
        data_list = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70]
        self.assertEqual(Part2.equal_depth_boundaries(data_list, 4), [[13, 16, 16, 16], [19, 21, 21, 21], [22, 22, 25, 25], [25, 25, 33, 33], [33, 35, 35, 35], [35, 35, 45, 45], [46, 46, 70]])


class TestEqWidthMedians(unittest.TestCase):
    def assert_floats_equal(self, list1, list2):
        for i in range(0, len(list1)):
            self.assertAlmostEqual(list1[i], list2[i], 4)

    def test1(self):
        data_list = [4, 8, 15, 21, 21, 24, 25, 28, 34]
        bin_list = Part2.equal_width_median(data_list, 10, 4, 34)
        self.assert_floats_equal([6.0, 21.0, 25.0, 34.0], bin_list)


    def test2(self):
        data_list = [4, 8, 15, 21, 21, 24, 25, 28, 34]
        self.assertEqual(Part2.equal_width_median(data_list, 10, 14, 30), [21, 25])

    def test3(self):
        data_list = [98, 99, 100, 101]
        self.assertEqual(Part2.equal_width_median(data_list, 3, 0, 10), [0, 0, 0, 0])

    def test4(self):
        data_list = [98, 99, 100, 101]
        self.assertEqual(Part2.equal_width_median(data_list, 3, 200, 210), [0, 0, 0, 0])

    def test5(self):
        data_list = [4, 8, 15, 21, 21, 24, 25, 28, 34]
        self.assertEqual(Part2.equal_width_median(data_list, 3, 0, 24), [0, 4, 8, 0, 0, 15, 0, 21, 24])

    def test6(self):
        data_list = [4, 8, 15, 21, 21, 24, 25, 28, 34]
        self.assertEqual(Part2.equal_width_median(data_list, 3, 21, 50), [21, 24.5, 28, 0, 34, 0, 0, 0, 0, 0])

    def test7(self):
        data_list = [13, 15, 16, 16, 19, 20, 20, 21, 22, 22, 25, 25, 25, 25, 30, 33, 33, 35, 35, 35, 35, 36, 40, 45, 46, 52, 70, 99]
        self.assertEqual(Part2.equal_width_median(data_list, 10, 0, 99), [0, 16, 22, 35, 45, 52, 0, 70, 0, 99])


class TestGetRanges(unittest.TestCase):
    def test1(self):
        self.assertEqual(Part2.get_ranges(10, 0, 99), [range(0, 10), range(10, 20), range(20, 30), range(30, 40), range(40, 50),
                                                   range(50, 60), range(60, 70), range(70, 80), range(80, 90), range(90, 100)])
    def test2(self):
        self.assertEqual(Part2.get_ranges(10, 4, 34), [range(4, 14), range(14, 24), range(24, 34), range(34, 35)])

    def test3(self):
        self.assertEqual(Part2.get_ranges(3, 0, 24), [range(0, 3), range(3, 6), range(6, 9), range(9, 12),
                                                      range(12, 15), range(15, 18), range(18, 21), range(21, 24), range(24, 25)])