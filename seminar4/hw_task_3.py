# 3.	Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
#
# [1, 2, 2, 3, 4]  -> [1, 3, 4]

user_set = [int(i) for i in input('Введите последовательность чисел: ').split()]
sl = {}
res_list = []

for el in user_set:
    sl[f'{el}'] = user_set.count(el)

for key, value in sl.items():
    if value == 1:
        res_list.append(int(key))

print(res_list)
