# 5.	Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
#
# Пример:
# o	для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите целое число: '))


def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


def neg_fib(n):
    if n == 0:
        return 0
    if n == 1:
        return neg_fib(n - 1) + 1
    else:
        return (neg_fib(n - 2) - neg_fib(n - 1))


list_fib = []
for el in range(1, num + 1):
    list_fib.append(fib(el))

list_neg_fib = []
for el in range(0, num + 1):
    list_neg_fib.append(neg_fib(el))

list_neg_fib.reverse()
print(list_neg_fib + list_fib)
