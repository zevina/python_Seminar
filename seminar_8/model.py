import csv
import logging


def import_file(path):
    with open(path, encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        return list(reader)


def add_employees_to_list(employees):
    with open('file.csv', 'a', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        writer.writerow(employees)


def update_employees(number, string):
    try:
        with open('file.csv', 'r', encoding='utf-8', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=';')
            data = list(reader)
            data[number] = string
        with open('file.csv', 'w', encoding='utf-8', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=';')
            for i in data:
                writer.writerow(i)
    except IndexError:
        logging.warning('Вы вышли за границы массива!')
        print('Вы вышли за границы массива!')
        exit()
    except Exception:
        logging.warning('Ошибка!')
        print('Ошибка!')
        exit()


def delete(number):
    with open('file.csv', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')
        data = list(reader)
        del data[number]
    with open('file.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)


def export_csv(data):
    with open('Employees_list.csv', 'w', encoding='utf-8', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=';')
        for i in data:
            writer.writerow(i)