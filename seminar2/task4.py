# 4. Напишите программу, которая проверяет пятизначное число на палиндром.

n1 = input('Введите число: ')

# if n[0] == n[-1] and n[1] == n[-2]:
#     print('Число является палиндромом')
# else:
#     print('Число не является палиндромом')

# count = 0
# for i in range(len(n) // 2):
#     if n[i] == n[-i - 1]:
#         count += 1
#
# if count == len(n) // 2:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# f = 1
# for i in range(len(n) // 2):
#     if n[i] != n[-i - 1]:
#         print('Не палиндром')
#         f = 0
#         break
#
# if f:
#     print('Палиндром')

n2 = n1[::-1]
if n2 == n1:
    print('Палиндром')
else:
    print('Не палиндром')
