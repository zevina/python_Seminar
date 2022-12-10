# 2.	Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежат конфеты. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота "интеллектом"

import random
import time


# игра, когда бот ходит первым
def game_1(candy, k):
    sp = []
    print('\n' + 'Первым ходит бот --->', end='')
    b = candy % (k + 1)
    if b > 0:
        print(f' Бот взял {b}')
        candy -= b
        print(f'В куче осталось {candy} конфет')
        hod = 2
    else:
        b = random.randint(1, k + 1)
        print(f' Бот взял {b}')
        candy -= b
        print(f'В куче осталось {candy} конфет')
        game_2(candy, k)
    while candy > k:
        if hod == 1:
            b = (k + 1) - sp[-1]
            print('\n' + f'Ход бота --->  Бот взял {b}')
            candy -= b
            print(f'В куче осталось {candy} конфет')
            hod = 2
        elif hod == 2:
            x = int(input('\n' + 'Ход игрока ---> Введите количество конфет: '))
            if 0 < x <= k:
                candy -= x
                sp.append(x)
                print(f'В куче осталось {candy} конфет')
                hod = 1
            else:
                print(f'Максимальное количество конфет за один ход {k}')
    if hod == 1:
        print('Победил бот!')
    else:
        print('Победил игрок!')


# игра, когда бот ходит вторым
def game_2(candy, k):
    f = False
    sp = []
    x = int(input('Ход игрока ---> Введите количество конфет: '))
    if 0 < x <= k:
        if x == candy % (k + 1):
            f = True
        candy -= x
        print(f'В куче осталось {candy} конфет')
        sp.append(x)
        hod = 1
    else:
        print(f'Максимальное количество конфет за один ход {k}')
    if f:
        b = random.randint(1, k + 1)
        print('\n' + f'Ход бота --->  Бот взял {b}')
        candy -= b
        print(f'В куче осталось {candy} конфет')
        hod = 2
    else:
        b = candy % (k + 1)
        print(f' Бот взял {b}')
        candy -= b
        print(f'В куче осталось {candy} конфет')
        hod = 2
    while candy > k:
        if hod == 1:
            b = (k + 1) - sp[-1]
            print('\n' + f'Ход бота --->  Бот взял {b}')
            candy -= b
            print(f'В куче осталось {candy} конфет')
            hod = 2
        elif hod == 2:
            x = int(input('\n' + 'Ход игрока ---> Введите количество конфет: '))
            if 0 < x <= k:
                candy -= x
                sp.append(x)
                print(f'В куче осталось {candy} конфет')
                hod = 1
            else:
                print(f'Максимальное количество конфет за один ход {k}')
    if hod == 1:
        print('Победил бот!')
    else:
        print('Победил игрок!')


candy = random.randint(100, 200)
print('\n' + f'На столе {candy} конфет')
k = random.randint(20, 31)
print(f'Брать можно не больше {k} конфет!')

print('\n' + 'Жеребьевка.', end='')
time.sleep(1)
print('.', end='')
time.sleep(1)
print('.')

hod = random.randint(1, 2)
if hod == 1:
    game_1(candy, k)
if hod == 2:
    game_2(candy, k)


