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
