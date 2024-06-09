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
    while m % 4 == 0:
        divisible_a = (a % 4 == 0)
        divisible_b = (m % 4 == 0)
        if divisible_a and divisible_b:
            break
        else:
            a += 1
    return True, a


def inspect(a, c, m):
    a -= 1

    k = 0
    while k != 1:
        k = math.gcd(c, m)
        if k != 1:
            c += 1

    n = False
    l = False
    while not n or not l:
        p = check_divisibility_by_4(a, m)
        l = p[0]
        a = p[1]
        n = all_prime_factors(a, m)
        if not n or not l:
            a += 1
    result = [a+1, c, m]
    return result
