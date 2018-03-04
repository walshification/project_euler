import unittest

from solutions import smallest_multiple


class SmallestMultipleTests(unittest.TestCase):
    def test_smallest_evenly_divisible_retuns_smallest_one(self):
        self.assertEqual(smallest_multiple.smallest_evenly_divisible(10), 2520)

    def test_get_prime_factorize_returns_prime_factors_of_number(self):
        self.assertCountEqual(smallest_multiple.prime_factorize(20), [2, 2, 5])
        self.assertCountEqual(smallest_multiple.prime_factorize(18), [2, 3, 3])
        self.assertCountEqual(smallest_multiple.prime_factorize(9), [3, 3])

    def test_minimum_viable_factors_returns_minimum_number_of_factors_for_numbers(self):
        factors = smallest_multiple.minimum_viable_factors([10, 9])
        self.assertCountEqual(factors, [2, 5, 3, 3])

    def test_returns_correct_factors_for_overlapping_factor_groups(self):
        factors = smallest_multiple.minimum_viable_factors([15, 9])
        self.assertCountEqual(factors, [3, 5, 3])
