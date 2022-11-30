# 2.	Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#
# Пример:
# o	[2, 3, 4, 5, 6] => [12, 15, 16];
# o	[2, 3, 5, 6] => [12, 15]

import random

random_list = []
for i in range(0, 5):
    n = random.randint(0, 9)
    random_list.append(n)

multi_list = []
for i in range(0, len(random_list) // 2 + 1):
    p = (random_list[i] * random_list[len(random_list) - i - 1])
    multi_list.append(p)

print('Сгенерированный список: ', random_list)
print(multi_list)
