# 1.	Задайте строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# user_str = input('Введите набор чисел: ')
# user_set = user_str.split(' ')

try:
    user_set = [int(i) for i in input('Введите набор чисел: ').split()]
    for i in range(len(user_set)):
        user_set[i] = int(user_set[i])
    max_digit = max(user_set)
    min_digit = min(user_set)
    print(f'наибольшее число: {max_digit} \nнаименьшее число: {min_digit}')
except ValueError:
    print('Вы ввели НЕ число! Goodbye')




