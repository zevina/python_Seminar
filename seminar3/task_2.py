# 2.	Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.

# Входные данные
# 1 5 2 4 3
#
# Выходные данные
# 5
# 4

sp_1 = [1, 5, 2, 4, 3]
print(sp_1)

for i in range(1, len(sp_1)):
    if sp_1[i] > sp_1[i - 1]:
        print(sp_1[i])