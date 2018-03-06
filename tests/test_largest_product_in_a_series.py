import unittest

from solutions import largest_product_in_a_series


class LargestProductInASeriesTests(unittest.TestCase):
    def test_subseries_returns_all_valid_slices_of_series(self):
        subseries = largest_product_in_a_series.subseries(2, [1, 2, 3, 4, 5])
        expected_series = [
            [1, 2],
            [2, 3],
            [3, 4],
            [4, 5],
        ]
        self.assertCountEqual(subseries, expected_series)

    def test_largest_product_returns_largest_subseries_combo(self):
        largest = largest_product_in_a_series.largest_product(2, [1, 2, 5, 4, 3])
        self.assertEqual(largest, 20)
