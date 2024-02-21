# 1
def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def is_coprime(x, y):
    return greatest_common_divisor(x, y) == 1


def count_coprime_numbers(n):
    count = 0
    for i in range(1, n + 1):
        if is_coprime(n, i):
            count += 1
    return count


# 2
def sum_digits_divisible_by_three(number):
    total = 0
    while number > 0:
        digit = number % 10
        if digit % 3 == 0:
            total += digit
        number //= 10
    return total
