'''
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
'''


def sum_to_limit(limit=1000):
    return sum(i for i in generate_to_limit(limit))


def generate_to_limit(limit):
    for i in range(3, limit):
        if i % 3 == 0 or i % 5 == 0:
            yield i


if __name__ == '__main__':
    print(sum_to_limit())  # => 233168
