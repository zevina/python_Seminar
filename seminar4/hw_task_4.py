# 4.	Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.
#
# Пример:
# o	k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

k = int(input('Введите степень k: '))

random_coef = []
for i in range(0, k + 1):
    n = random.randint(0, 9)
    random_coef.append(n)


# функция возвращает многочлен на основе списка коэффициентов
def create_mn(k, coef):
    mn = []
    for i in range(0, len(coef) - 2):
        if coef[i] == 0:
            continue
        elif coef[i] == 1:
            x = f'x^{k - i}'
        else:
            x = f'{coef[i]}x^{k - i}'
        mn.append(x)
    for i in range(len(coef) - 2, len(coef) - 1):
        if coef[i] == 0:
            continue
        elif coef[i] == 1:
            x = 'x'
        else:
            x = f'{coef[i]}x'
        mn.append(x)
    for i in range(len(coef) - 1, len(coef)):
        if coef[i] == 0:
            continue
        else:
            x = f'{coef[i]}'
        mn.append(x)
    return mn


res_mn = ' + '.join(create_mn(k, random_coef)) + ' = 0'
print(res_mn)

with open('for_task_4.txt', 'w') as file:
    file.write(res_mn)
