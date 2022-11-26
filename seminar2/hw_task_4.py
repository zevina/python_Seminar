# 4. Задайте числами список из N элементов, заполненных из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число N: '))
sp = []

for i in range(-n, n+1):
    sp.append(i)

print(sp)

pr = 1
try:
    with open('file.txt') as f:
        for line in f:
            pr *= sp[int(line)]
    print(pr)
except FileNotFoundError:
    print('Файл не найден!')
finally:
    f.close()
