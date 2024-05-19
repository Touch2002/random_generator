from sympy import primefactors
import math


def inspect(a, c, m):
    k = 0
    while k != 1:
        k = find_gcd(c, m)
        if k != 1:
            c += 1

    n = False
    while not n:
        n = all_prime_factors(a-1, 2 ^ 17)
        a += 1
        print(n, a)



    result = [a, c]
    return result



def all_prime_factors(n, m):
    """Перевірка, чи число n ділиться на всі прості дільники числа m"""
    prime_factors = primefactors(m)
    for factor in prime_factors:
        if n % factor != 0:
            return False
    return True


k = 289
n = False
while not n:
    n = all_prime_factors(k-1, 2^17)
    k += 1
    print(n, k)


def find_gcd(a, b):
    return math.gcd(a, b)


def test():
    # Приклади використання
    m = 30
    n1 = 60
    n2 = 10
    print(all_prime_factors(n1, m))  # True, оскільки 60 ділиться на 2, 3 і 5
    print(all_prime_factors(n2, m))  # False, оскільки 10 не ділиться на 3
    print(all_prime_factors(1079, 2 ^ 17))

    # Приклад використання
    a = 289
    b = 2 ^ 17
    print(f"НСД({a}, {b}) = {find_gcd(a, b)}")

    print(inspect(289, 1079, 2 ^ 17))
test()