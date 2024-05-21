from sympy import primefactors
import math


def all_prime_factors(a, m):
    """Перевірка, чи число a ділиться на всі прості дільники числа m"""
    prime_factors = primefactors(m)
    for factor in prime_factors:
        if a % factor != 0:
            return False
    return True


def check_divisibility_by_4(a, m):
    while True:
        divisible_a = (a % 4 == 0)
        divisible_b = (m % 4 == 0)
        if (divisible_a and divisible_b) or (not divisible_a and not divisible_b):
            return True, a
        else:
            a += 1


def inspect(a, c, m):
    k = 0
    while k != 1:
        k = math.gcd(c, m)
        if k != 1:
            c += 1
    n = False
    l = False
    while not n:
        p = check_divisibility_by_4(a-1, m)
        l = p[0]
        n = all_prime_factors(p[1], 2 ** 17)
        if not n or not l:
            a += 1
    result = [a, c, m]
    return result

