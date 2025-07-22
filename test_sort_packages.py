import unittest
from sort_packages import sort

class TestSortFunction(unittest.TestCase):
    def test_standard(self):
        self.assertEqual(sort(100, 100, 50, 10), "STANDARD")

    def test_bulky_only_by_volume(self):
        self.assertEqual(sort(100, 100, 100, 10), "SPECIAL")

    def test_bulky_only_by_dimension(self):
        self.assertEqual(sort(150, 10, 10, 5), "SPECIAL")

    def test_heavy_only(self):
        self.assertEqual(sort(10, 10, 10, 25), "SPECIAL")

    def test_rejected(self):
        self.assertEqual(sort(200, 200, 200, 25), "REJECTED")

    def test_edge_case_exact_limits(self):
        self.assertEqual(sort(150, 10, 10, 20), "REJECTED")

if __name__ == '__main__':
    unittest.main()
