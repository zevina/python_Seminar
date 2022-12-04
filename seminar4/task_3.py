# 3.	Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

num_1 = int(input('Введите первое число: '))
num_2 = int(input('Введите второе число: '))

big = max(num_1, num_2)

while (True):
    if big % num_1 == 0 and big % num_2 == 0:
        res = big
        break
    big += 1

print(res)

# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
#
# p = a * b
# while a != 0 and b != 0:
#     if a > b:
#         a = a % b
#     else:
#         b = b % a
#
# nod = a + b
# nok = p // nod
# print(nok)