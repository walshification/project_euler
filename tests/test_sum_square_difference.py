import unittest

from solutions import sum_square_difference


class SumSquareDifference(unittest.TestCase):
    def test_sum_of_the_squares_of_integers_returns_the_sum(self):
        total = sum_square_difference.sum_of_the_squares_of_integers([1, 2, 3])
        self.assertEqual(total, 14)

    def test_square_of_the_sum_returns_the_thing(self):
        total = sum_square_difference.square_of_the_sum([1, 2, 3])
        self.assertEqual(total, 36)

    def test_difference_returns_the_sum_of_squares_minus_square_of_sum(self):
        difference = sum_square_difference.difference_of_the_sum_the_squares(3)
        self.assertEqual(difference, 22)
