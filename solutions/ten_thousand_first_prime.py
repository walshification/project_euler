'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10,001st prime number?
'''
import math


def get_prime(n):
    current = 1
    primes_generator = generate_primes(n)
    while current < n:
        next(primes_generator)
        current += 1
    return next(primes_generator)


def generate_primes(limit):
    yield 2
    composites = {}
    prime = 3
    limit = int(limit * math.log(limit) * 10)  # approximish

    while 1:
        if not composites.get(prime):
            for composite in generate_composites(prime, limit):
                composites[composite] = True
            yield prime
        prime += 2


def generate_composites(base, limit):
    for i in range(base, limit + 1, base):
        yield i


if __name__ == '__main__':
    print(get_prime(10001))  # => 104743
