import logging


def show_menu():
    print('Выберете команду:\n1 - импорт\n2 - экспорт')
    try:
        select = int(input())
        if select not in [1, 2]:
            raise ValueError
        return select
    except Exception:
        print("Команда выбрана некорректно!")
        logging.warning('Команда выбрана некорректно!')


def show_data(data):
    for i in range(len(data)):
        if i == 0:
            for key in data[i]:
                print('  ' + key, end=' ')
            print()
            print(i + 1, end=' ')
            for key, value in data[i].items():
                print(value, end=' ')
        else:
            print(i + 1, end=' ')
            for key, value in data[i].items():
                print(value, end=' ')
        print()


def import_export_menu():
    print('Выберете формат файла:\n1 - .txt\n2 - .csv')
    try:
        select = int(input())
        if select not in [1, 2]:
            raise ValueError
        return select
    except Exception:
        print("Формат выбран некорректно!")
        logging.warning('Формат выбран некорректно!')


def path_file():
    path_file = input('Введите путь к файлу: ')
    return path_file
