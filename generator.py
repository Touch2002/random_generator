def inspect(a, c, m):
    result = True
    return result


def gen_xi(x0, a, c, m):
    xi_list = [x0,]
    x = x0
    for i in range(4095):
        xi = (a * x + c) % m
        xi_list.append(xi)
        x = xi
    return xi_list


def gen_result(xi_list):
    yi_list = []
    for i in xi_list:
        yi_list.append(i / 4 % 4095)
    return yi_list

if __name__ == '__main__':
    q = gen_xi(0, 289, 1084, 2**17)
    print(q, len(q))