import unittest

from solutions import multiples_of_3_and_5


class MultiplesOf3And5Tests(unittest.TestCase):
    def test_generate_to_list_creates_multiples_excluding_a_given_limit(self):
        multiples = list(multiples_of_3_and_5.generate_to_limit(20))
        self.assertEqual(multiples, [3, 5, 6, 9, 10, 12, 15, 18])

    def test_sum_to_limit_returns_sum_of_all_the_returned_multiples(self):
        total = multiples_of_3_and_5.sum_to_limit(10)
        self.assertEqual(total, 23)
