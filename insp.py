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
        print(n, a, "inspect")


    result = [a, c, m]
    print(result, "Inspect")
    return result


def test():
    # Приклади використання
    m = 30
    n1 = 60
    n2 = 10
    print(all_prime_factors(n1, m))  # True, оскільки 60 ділиться на 2, 3 і 5
    print(all_prime_factors(n2, m))  # False, оскільки 10 не ділиться на 3
    print(all_prime_factors(1079, 2 ** 17))

    # Приклад використання
    a = 289
    b = 2 ** 17
    print(f"НСД({a}, {b}) = {math.gcd(a, b)}")

    print(inspect(169, 857, 2 ** 20))

    # Приклади використання
    num1 = 16
    num2 = 20
    num3 = 15
    num4 = 9

    print(f"{num1} і {num2}: {check_divisibility_by_4(num1, num2)}")  # True, обидва діляться на 4
    print(f"{num1} і {num3}: {check_divisibility_by_4(num1, num3)}")  # False, тільки одне число ділиться на 4
    print(f"{num3} і {num4}: {check_divisibility_by_4(num3, num4)}")  # True, жодне не ділиться на 4
    print(f"{num2} і {num4}: {check_divisibility_by_4(num2, num4)}")  # False, тільки одне число ділиться на 4
test()
