# 2.	Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.


n = int(input('Введите натуральное число N: '))
res_list = []

dl = 2
while dl <= n:
    if n % dl == 0:
        n /= dl
        res_list.append(dl)
    else:
        dl += 1

print(res_list)
