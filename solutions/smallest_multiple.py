'''
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all
of the numbers from 1 to 20?
'''


# from solutions.largest_prime_factor import generate_prime_factors


def smallest_evenly_divisible(number, factors=None):
    # prime_factors_for_all = minimum_viable_factors(range(1, number))

    factors = factors or [19, 18, 17, 16, 15, 14, 13, 12, 11]
    start = number * number
    for i in range(start, 1000000000+1, number):
        if is_superfactor(i, factors):
            return i


# def minimum_viable_factors(numbers):
#     factor_groups = [prime_factorize(number) for number in numbers]
#     all_factors = [factor for factor_group in all_factors for factor in factor_group]
#     minimum_factors = []
#     for factor_group in factor_groups:
#         for factor in


# def prime_factorize(number, factors=None):
#     factors = factors or list(generate_prime_factors(number))
#     for factor in factors:
#         if number % factor == 0:
#             divided = number / factor
#             return [factor] + prime_factorize(divided, factors)
#     return []


def is_superfactor(number, factors):
    return all(number % i == 0 for i in factors)


if __name__ == '__main__':
    print(smallest_evenly_divisible(20))  # => 232792560
