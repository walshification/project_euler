'''
A palindromic number reads the same both ways. The largest palindrome
made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''


def for_n_digit_numbers(n=3):
    limit = calculate_limit(n)
    multipliers = []
    largest = 0
    for i in range(limit, 0, -1):
        multipliers.append(i)
        for multiplier in multipliers:
            product = multiplier * i
            if is_palindrome(product) and product > largest:
                largest = product
    return largest


def calculate_limit(n):
    limit = 1
    for _ in range(n):
        limit *= 10
    return limit - 1


def is_palindrome(number):
    number_string = str(number)
    return number_string == number_string[::-1]


if __name__ == '__main__':
    print(for_n_digit_numbers())  # => 906609
