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
        yi_list.append(int(i / 4 % 4095))
    return yi_list


def save_result(yi_list, file_name):
    with open(file_name + '.txt', 'w') as file:
        for i in yi_list:
            file.write(f"{i}\n")  # Записуємо число у файл з новим рядком


def generate(x0, acmlist, file_name):
    a, c, m = acmlist[0], acmlist[1], acmlist[2]
    xi_l = gen_xi(x0, a, c, m)
    yi_l = gen_result(xi_l)
    save_result(yi_l, file_name)
