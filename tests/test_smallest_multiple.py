import unittest

from solutions import smallest_multiple


class SmallestMultipleTests(unittest.TestCase):
    def test_is_superfactor_returns_true_if_number_is_evenly_divisible_by_all_factors(self):
        self.assertTrue(smallest_multiple.is_superfactor(12, [2, 3, 4]))

    def test_is_superfactor_returns_false_if_number_isnt_evenly_divisible_by_a_factor(self):
        self.assertFalse(smallest_multiple.is_superfactor(12, [2, 3, 4, 5]))

    def test_smallest_evenly_divisible_retuns_smallest_one(self):
        self.assertEqual(smallest_multiple.smallest_evenly_divisible(10, [9, 8, 7, 6]), 2520)

    # def test_get_prime_factorize_returns_prime_factors_of_number(self):
    #     self.assertEqual(smallest_multiple.prime_factorize(20), [2, 2, 5])
    #     self.assertEqual(smallest_multiple.prime_factorize(18), [2, 3, 3])
    #     self.assertEqual(smallest_multiple.prime_factorize(9), [3, 3])

    # def test_minimum_viable_factors_returns_minimum_number_of_factors_for_numbers(self):
    #     self.assertEqual(smallest_multiple.minimum_viable_factors([10, 9]), [2, 5, 3, 3])
