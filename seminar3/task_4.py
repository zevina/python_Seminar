# 4.	Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
#
# Входные данные
# 12
# Строка1
# Строка2
# Строка3
# Строка45
# Стр12ка
#
# Выходные данные
# да

# sp = [12, 'str1', 'str2', 'str3', 'str45']
# print(sp)
# f = 'нет'
#
# for i in range(len(sp)):
#     if type(sp[i]) == int:
#         f= 'да'
#         break
#
# print(f)

# list = []
# number = 12
#
# f = 'нет'
#
# for i in range(5):
#     list.append(input('Введите элемент списка: '))
#
# for i in range(len(list)):
#     if str(number) in list[i]:
#         f = 'да'
#         break
#
# print(f)

list = []
number = 12
for i in range(5):
    list.append(input('Введите элемент списка: '))

if any(str(number) in el for el in list):
    print('да')
else:
    print('нет')
