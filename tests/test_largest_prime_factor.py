import unittest

from solutions import largest_prime_factor


class LargestPrimeFactorTests(unittest.TestCase):
    def test_generate_prime_factors_to_limit_returns_list_of_factors(self):
        prime_factors = list(largest_prime_factor.generate_prime_factors(100))
        self.assertEqual(prime_factors, [2, 5])

    def test_generate_composites_returns_multiples_for_number_up_to_a_limit(self):
        composites = list(largest_prime_factor.generate_composites(2, 10))
        self.assertEqual(composites, [2, 4, 6, 8, 10])

    def test_find_largest_of_number_returns_largest_prime_factor_of_a_given_number(self):
        largest = largest_prime_factor.find_largest_of_number(105)
        self.assertEqual(largest, 7)
