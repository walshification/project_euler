'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
'''


import math


def find_largest_of_number(number):
    return [prime for prime in generate_prime_factors(number)][-1]


def generate_prime_factors(number):
    factor_limit = math.ceil(math.sqrt(number)) + 1
    prime_factors = []
    if number % 2 == 0:
        prime_factors.append(2)
    composites = {}

    for prime in range(3, factor_limit, 2):
        if not composites.get(prime):
            for composite in generate_composites(prime, factor_limit):
                composites[composite] = True
            if number % prime == 0:
                prime_factors.append(prime)

    return prime_factors


def generate_composites(base, limit):
    for i in range(base, limit + 1, base):
        yield i


if __name__ == '__main__':
    print(find_largest_of_number(600851475143))  # => 6857
