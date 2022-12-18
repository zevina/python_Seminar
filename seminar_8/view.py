import logging


def show_menu():
    print("Выберите команду:\n1 - показать сотрудников\n2 - добавить сотрудника\n3 - изменить данные\n4 - удалить сотрудника\n5 - экспорт данных в файл")
    try:
        select = int(input())
        if select not in [1, 2, 3, 4, 5]:
            raise ValueError
        return select
    except Exception:
        print("Команда выбрана некорректно!")
        logging.warning('Команда выбрана некорректно!')
        exit()


def show_employees(list):
    print("Список всех сотрудников:")
    for i, el in enumerate(list):
        if i == 0:
            print(' ', *el)
        else:
            print(i, *el)


def add_employees():
    print("Введите данные сотрудника (фамилия, имя, телефон, должность) через пробел:")
    data = input().split()
    return data


def change_employees():
    print("Выберите строку для перезаписи:")
    change = int(input())
    print("Введите новые данные сотрудника (фамилия, имя, телефон, должность) для перезаписи через пробел:")
    string = input().split()
    return change, string


def delete():
    print("\nВыберите строку для удаления:")
    number = int(input())
    return number


def path_file():
    path_file = input('Введите путь к файлу: ')
    return path_file