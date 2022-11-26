# 5. Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя, другие методы из библиотеки random - можно)

import random

n = int(input('Введите длину списка N: '))
sp = []

for i in range(n):
    a = random.randint(0, 9)
    sp.append(a)

print('Cгенерированный рандомный список в границах : ', sp)


for i in range(0, len(sp)):
    random_index = random.randint(0,len(sp) - 1)
    sp[i], sp[random_index] = sp[random_index], sp[i]

print('Перемешанный рандомный список: ', sp)