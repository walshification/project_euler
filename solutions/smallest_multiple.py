'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''
from collections import defaultdict
from functools import reduce

from solutions.largest_prime_factor import generate_prime_factors


def smallest_evenly_divisible(number):
    '''
    Returns the smallest positive number that is evenly divisible by
    all numbers in a given set.
    '''
    prime_factors_for_all = minimum_viable_factors(range(2, number+1))
    return reduce(lambda a, b: a * b, prime_factors_for_all)


def minimum_viable_factors(numbers):
    '''
    Returns the smallest set of prime factors for a given set of
    numbers.
    '''
    factor_groups = [prime_factorize(number) for number in numbers]
    return __filter_redundant_factors(factor_groups)


def prime_factorize(number, factors=None):
    '''Returns the prime factors for a given number.'''
    if number == 1:
        return []
    factors = factors or list(generate_prime_factors(number))
    if factors:
        factor = factors.pop()
        divided = number // factor
        return [factor] + prime_factorize(divided, factors)
    return [number]  # is prime


def __filter_redundant_factors(factor_groups):
    minimum_factors = []
    for factor_group in factor_groups:
        factor_count = defaultdict(int)
        for factor in factor_group:
            factor_count[factor] += 1
            # add the factor if we don't already have enough
            if factor_count[factor] > minimum_factors.count(factor):
                minimum_factors.append(factor)
    return minimum_factors


if __name__ == '__main__':
    print(smallest_evenly_divisible(20))  # => 232792560
