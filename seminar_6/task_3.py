# 3.	Дан список чисел. Вывести из него только простые числа.
#
# Ввод
# 15 2 3 31
#
# Вывод
# 2 3 31


def prime_num(n):
    res = []
    d = 2
    while d <= n ** 0.5:
        if n % d == 0:
            res.append(d)
            k = n //d
            if k != d:
                res.append(k)
        d += 1
    return not res


num = input('Введите числа через пробел: ').split()

for i in range(len(num)):
    num[i] = int(num[i])

num = list(filter(lambda x: prime_num(x), num))

print(num)
