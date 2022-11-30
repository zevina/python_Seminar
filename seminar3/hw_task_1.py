# 1.	Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
#
# Пример:
# 	[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12
import random

random_list = []
for i in range(0, 10):
    n = random.randint(0, 9)
    random_list.append(n)

sum = 0
for i in range(1, len(random_list), 2):
    sum += random_list[i]

print('Сгенерированный список: ', random_list)
print('Cумма элементов списка, стоящих на нечётной позиции =', sum)