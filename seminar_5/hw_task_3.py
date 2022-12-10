# 3.	Создайте программу для игры в "Крестики-нолики".


def print_m(mat):
    print('\n' * 100)
    print(' ' + '_' * 20)
    print('|' + ' ' * 6 + '|' + ' ' * 6 + '|' + ' ' * 6 + '|')
    print('|', end='')
    print(*mat[0], sep='|', end='')
    print('|')
    print('|' + '_' * 6 + '|' + '_' * 6 + '|' + '_' * 6 + '|')
    print('|' + ' ' * 6 + '|' + ' ' * 6 + '|' + ' ' * 6 + '|')
    print('|', end='')
    print(*mat[1], sep='|', end='')
    print('|')
    print('|' + '_' * 6 + '|' + '_' * 6 + '|' + '_' * 6 + '|')
    print('|' + ' ' * 6 + '|' + ' ' * 6 + '|' + ' ' * 6 + '|')
    print('|', end='')
    print(*mat[2], sep='|', end='')
    print('|')
    print('|' + ' ' * 6 + '|' + ' ' * 6 + '|' + ' ' * 6 + '|')
    print(' ' + '‾' * 20)


def step_m(mat, x, znak):
    f = False
    while not f:
        if x == 1:
            if ('   X  ' not in mat[0][0]) and ('   O  ' not in mat[0][0]):
                mat[0][0] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
        if x == 2:
            if ('   X  ' not in mat[0][1]) and ('   O  ' not in mat[0][1]):
                mat[0][1] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
        if x == 3:
            if ('   X  ' not in mat[0][2]) and ('   O  ' not in mat[0][2]):
                mat[0][2] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
        if x == 4:
            if ('   X  ' not in mat[1][0]) and ('   O  ' not in mat[1][0]):
                mat[1][0] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
        if x == 5:
            if ('   X  ' not in mat[1][1]) and ('   O  ' not in mat[1][1]):
                mat[1][1] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
        if x == 6:
            if ('   X  ' not in mat[1][2]) and ('   O  ' not in mat[1][2]):
                mat[1][2] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
        if x == 7:
            if ('   X  ' not in mat[2][0]) and ('   O  ' not in mat[2][0]):
                mat[2][0] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
        if x == 8:
            if ('   X  ' not in mat[2][1]) and ('   O  ' not in mat[2][1]):
                mat[2][1] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
        if x == 9:
            if ('   X  ' not in mat[2][2]) and ('   O  ' not in mat[2][2]):
                mat[2][2] = znak
                f = True
            else:
                print('Некорректный ход!')
                x = int(input('введите номер позиции для хода: '))
    return mat


def victory(sp):
    flag = False
    if sp[0][0] == sp[1][1] == sp[2][2] or \
            sp[2][0] == sp[1][1] == sp[0][2] or \
            sp[0][0] == sp[1][0] == sp[2][0] or \
            sp[0][1] == sp[1][1] == sp[2][1] or \
            sp[0][2] == sp[1][2] == sp[2][2] or \
            sp[0][0] == sp[0][1] == sp[0][2] or \
            sp[1][0] == sp[1][1] == sp[1][2] or \
            sp[2][0] == sp[2][1] == sp[2][2]:
        flag = True
    return flag


sp = [['   1  ', '   2  ', '   3  '], ['   4  ', '   5  ', '   6  '], ['   7  ', '   8  ', '   9  ']]
print_m(sp)

count = 0
znak = True
while not victory(sp):
    if count <= 8:
        step = int(input('введите номер позиции для хода: '))
        if znak:
            sp = step_m(sp, step, '   X  ')
            print_m(sp)
            znak = not znak
            count += 1
        else:
            print_m(step_m(sp, step, '   O  '))
            znak = not znak
            count += 1
    else:
        print('Ничья!')
        break

if victory(sp):
    if znak:
        print('Победили нолики - О')
    else:
        print('Победили крестики - Х')
