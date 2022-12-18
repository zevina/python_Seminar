import csv
import logging


def import_csv_file(path):
    with open(path, encoding='utf8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        return list(reader)


def import_txt_file(path):
    with open(path, 'r', encoding='utf-8') as data:
        list_1 = data.read().split('\n\n')
    list_2 = []
    list_3 = []
    count = 0
    i = 0
    while i < len(list_1):
        while count < 4:
            list_2.append(list_1[i])
            count += 1
            i += 1
        list_3.append(list_2)
        list_2 = []
        count = 0
    list_4 = []
    for i in range(len(list_3) - 1):
        dic = {list_3[0][0]: list_3[i + 1][0],
               list_3[0][1]: list_3[i + 1][1],
               list_3[0][2]: list_3[i + 1][2],
               list_3[0][3]: list_3[i + 1][3]}
        list_4.append(dic)
        dic = {}
    return list_4


def export_csv(data):
    with open('Phonebook.csv', 'w', encoding='utf8', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=list(data[0].keys()), delimiter=';')
        writer.writeheader()
        for i in data:
            writer.writerow(i)


def export_txt(data):
    with open('Phonebook.txt', 'w', encoding='utf-8') as file:
        for i in range(len(data)):
            if i == 0:
                for key in data[i]:
                    file.write(key + '\n\n')
                for key, value in data[i].items():
                    file.write(value + '\n\n')
            else:
                for key, value in data[i].items():
                    file.write(value + '\n\n')
