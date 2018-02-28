import unittest

from solutions import even_fibonacci_numbers


class EvenFibonacciTests(unittest.TestCase):
    def test_next_pair_returns_next_even_fibonacci_numbers(self):
        pair = even_fibonacci_numbers.next_pair(8, 2)
        self.assertEqual(pair, (34, 8))

    def test_generate_to_limit_yields_even_numbers_to_the_given_limit(self):
        number_list = list(even_fibonacci_numbers.generate_to_limit(10))
        self.assertEqual(number_list, [2, 8])

    def test_generate_to_limit_includes_limit_if_limit_is_even(self):
        number_list = list(even_fibonacci_numbers.generate_to_limit(34))
        self.assertEqual(number_list, [2, 8, 34])

    def test_find_sum_to_limit_returns_sum_of_even_fibonacci_numbers_to_limit(self):
        total = even_fibonacci_numbers.sum_to_limit(limit=40)
        self.assertEqual(total, 44)
