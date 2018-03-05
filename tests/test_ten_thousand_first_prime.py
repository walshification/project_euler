import unittest

from solutions import ten_thousand_first_prime


class TenThousandFirstPrimeTests(unittest.TestCase):
    def test_get_prime_returns_2_as_first_prime(self):
        prime = ten_thousand_first_prime.get_prime(1)
        self.assertEqual(prime, 2)

    def test_get_prime_returns_3_as_second_prime(self):
        prime = ten_thousand_first_prime.get_prime(2)
        self.assertEqual(prime, 3)

    def test_get_prime_returns_5_as_second_prime(self):
        prime = ten_thousand_first_prime.get_prime(3)
        self.assertEqual(prime, 5)

    def test_get_prime_returns_13_as_the_6th_prime(self):
        prime = ten_thousand_first_prime.get_prime(6)
        self.assertEqual(prime, 13)
