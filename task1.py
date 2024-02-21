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


# 3
def find_divisor_with_max_coprime_digits(number):
    max_coprime_count = 0
    max_coprime_divisor = 1
    for i in range(2, number + 1):
        if number % i == 0:
            coprime_count = 0
            for digit in str(number):
                if is_coprime(int(digit), i):
                    coprime_count += 1
            if coprime_count > max_coprime_count:
                max_coprime_count = coprime_count
                max_coprime_divisor = i
    return max_coprime_divisor
