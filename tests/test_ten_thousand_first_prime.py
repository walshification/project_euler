import unittest

from solutions import ten_thousand_first_prime


class TenThousandFirstPrimeTests(unittest.TestCase):
    def test_get_target_prime_returns_2_as_first_prime(self):
        prime = ten_thousand_first_prime.get_target_prime(1)
        self.assertEqual(prime, 2)

    def test_get_target_prime_returns_3_as_second_prime(self):
        prime = ten_thousand_first_prime.get_target_prime(2)
        self.assertEqual(prime, 3)

    def test_get_target_prime_returns_5_as_second_prime(self):
        prime = ten_thousand_first_prime.get_target_prime(3)
        self.assertEqual(prime, 5)

    def test_get_target_prime_returns_13_as_the_6th_prime(self):
        prime = ten_thousand_first_prime.get_target_prime(6)
        self.assertEqual(prime, 13)

    def test_is_prime_returns_true_for_prime_numbers(self):
        for number in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]:
            with self.subTest(number=number):
                self.assertTrue(ten_thousand_first_prime.is_prime(number))

    def test_is_prime_returns_false_for_even_numbers_other_than_2(self):
        for number in [4, 6, 8, 10]:
            with self.subTest(number=number):
                self.assertFalse(ten_thousand_first_prime.is_prime(number))

    def test_is_prime_returns_false_for_odd_numbers_with_prime_factors(self):
        for number in [9, 15, 35]:
            with self.subTest(number=number):
                self.assertFalse(ten_thousand_first_prime.is_prime(number))
