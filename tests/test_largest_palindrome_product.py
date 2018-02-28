import unittest

from solutions import largest_palindrome_product


class LargestPalindromeProductTests(unittest.TestCase):
    def test_calculate_limit_returns_highest_possible_value_of_n_digits(self):
        self.assertEqual(largest_palindrome_product.calculate_limit(2), 99)
        self.assertEqual(largest_palindrome_product.calculate_limit(3), 999)

    def test_is_palindrome_returns_true_if_number_is_same_as_reversed(self):
        self.assertTrue(largest_palindrome_product.is_palindrome(1001))

    def test_for_n_digit_numbers_returns_largest_palindromic_product(self):
        self.assertEqual(largest_palindrome_product.for_n_digit_numbers(2), 9009)
