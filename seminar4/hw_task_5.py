# 5.	Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.


with open('for_task_5_1.txt') as f1:  # получаем 1й многочлен из одного файла
    first_mn = f1.read()

with open('for_task_5_2.txt') as f2:  # получаем 2й многочлен из другого файла
    second_mn = f2.read()

print(first_mn, second_mn, sep='\n')  # выводим исходные многочлены в терминал


# функция удаляет символы сложения и равенство нулю и возвращает список членов многочлена
def eliminate_symbols(mn):
    mn = mn.split()
    sp_mn = []
    for el in mn:
        if el == '+' or el == '=' or el == '0':
            continue
        else:
            sp_mn.append(el)
    return sp_mn


# функция возвращает словарь из членов многочлена со значением коэффициентов
def separate_mn(sp_mn):
    slov = {}
    for el in sp_mn:
        if 'x^' in el:
            cort = el.split('x')
            if cort[0] == '':
                slov[f'x{cort[1]}'] = '1'
            else:
                slov[f'x{cort[1]}'] = f'{cort[0]}'
        elif 'x' in el:
            cort = el.split('x')
            if cort[0] == '':
                slov[f'x{cort[1]}'] = '1'
            else:
                slov[f'x{cort[1]}'] = f'{cort[0]}'
        else:
            cort = (el, '^0')
            slov[f'{cort[1]}'] = f'{cort[0]}'
    return slov


# функция возвращает суммарный
def sum_mn(sl_1, sl_2):
    sum_sl = {}
    if len(sl_1) >= len(sl_2):
        big_sl = sl_1
        small_sl = sl_2
    else:
        big_sl = sl_2
        small_sl = sl_1
    for key, value in big_sl.items():
        if key in small_sl:
            sum_sl[key] = int(big_sl[key]) + int(small_sl[key])
        else:
            sum_sl[key] = int(big_sl[key])
    for key, value in small_sl.items():
        if key not in big_sl:
            sum_sl[key] = int(small_sl[key])
    sum_sl = dict(sorted(sum_sl.items(), key=lambda x: x[0], reverse=True))
    return sum_sl


# функция возвращает многочлен на основе суммарного словаря
def create_mn(sum_slov):
    mn = []
    for key, value in sum_slov.items():
        if value == 1:
            c = f'{key}'
        else:
            c = f'{value}{key}'
        if key == '^0':
            c = f'{value}'
        mn.append(c)
    return mn


slov_1 = separate_mn(eliminate_symbols(first_mn))
slov_2 = separate_mn(eliminate_symbols(second_mn))
res_sl = sum_mn(slov_1, slov_2)
result = ' + '.join(create_mn(res_sl)) + ' = 0'
print('\nСумма многочленов равна: ')
print(result)

with open('for_task_5_fin.txt', 'w') as file:
    file.write(result)
