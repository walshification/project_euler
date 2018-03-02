'''
The sum of the squares of the first ten natural numbers is,

1**2 + 2**2 + ... + 10**2 = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)**2 = 55**2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
'''


def difference_of_the_sum_the_squares(limit):
    return square_of_the_sum(range(1, limit+1)) - sum_of_the_squares_of_integers(range(1, limit+1))


def sum_of_the_squares_of_integers(integers):
    total = 0
    for integer in integers:
        total += integer**2
    return total


def square_of_the_sum(integers):
    return sum(integers) ** 2


if __name__ == '__main__':
    print(difference_of_the_sum_the_squares(100))
