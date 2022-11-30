# 3.	Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
#
# Пример:
# o	[1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

numb_list = []
dr_list = []
for i in range(0, 10):
    n = round(random.uniform(0, 9), random.randint(1, 2))
    n = (int(n * 100)) / 100
    numb_list.append(n)
for i in range(len(numb_list)):
    dr = (int(numb_list[i]*100)) % 100
    dr_list.append(dr)

max_dr = max(dr_list)
min_dr = min(dr_list)

print(numb_list)
print((max_dr - min_dr) / 100)
