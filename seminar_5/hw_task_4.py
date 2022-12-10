# 4.	Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
#
# Пример:
# Введите текст для кодировки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Текст после кодировки: 12W1B12W3B24W1B14W
# Текст после дешифровки: WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные и выходные данные хранятся в отдельных текстовых файлах.


# s = input('Введите текст для кодировки: ')

#РЕШЕНО СОВМЕСТНО С РЯБОВЫМ АНДРЕЕМ
import re

s = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
rle = []
count = 0

for i in range(0, len(s) - 1):
    if s[i] == s[i + 1]:
        count += 1
    elif s[i] != s[i + 1]:
        count += 1
        rle.append(count)
        rle.append(s[i])
        count = 0
    if i == (len(s) - 2) and s[-2] != s[-1]:
        rle.append(1)
        rle.append(s[i])
    elif i == (len(s) - 2) and s[-2] == s[-1]:
        count += 1
        rle.append(count)
        rle.append(s[i])

st = ''
for el in rle:
    st += str(el)

print('Текст после кодировки:', st)

with open('for_task_4.txt', 'w') as file:
    file.write(st)


# 2 часть задачи:
with open('for_task_4.txt') as file:
    part_2 = file.read()

sp2 = []
for i in range(len(part_2)):
    if part_2[i].isalpha():
        sp2.append(part_2[i])

rep = re.compile("[^0-9,\d]")
part_2 = rep.sub(" ", part_2)
sp1 = part_2.split()

res = ''
for i in range(len(sp1)):
    res += sp2[i] * int(sp1[i])

print('Текст после дешифровки:', res)

with open('for_task_4_2.txt', 'w') as file:
    file.write(res)

if s == res:
    print(True)
else:
    print(False)
