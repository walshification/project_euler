'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can
see that the 6th prime is 13.

What is the 10,001st prime number?
'''
import math


def get_target_prime(target):
    if target == 1:
        return 2  # handle the one even case

    candidate = 1
    count = 1  # 2 was our first counted prime
    while count != target:
        candidate += 2
        if is_prime(candidate):
            count += 1
    return candidate


def is_prime(number):
    if number < 4:  # 2 and 3
        return True
    if number % 2 == 0:  # any even number after 2
        return False

    # all primes after 3 are 6k +/- 1, where k == some constant
    limit = math.floor(math.sqrt(number))
    prime_factor = 3
    while prime_factor <= limit:
        if (number % prime_factor == 0) or (number % (prime_factor + 2) == 0):
            return False
        prime_factor += 6
    return True


if __name__ == '__main__':
    print(get_target_prime(10001))  # => 104743
