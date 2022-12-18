import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding="utf-8")


def main_function():
    select = view.show_menu()
    if select == 1:
        logging.info("Выбран импорт файла")
        format = view.import_export_menu()
        path = view.path_file()
        if format == 1:
            logging.info("Выбран формат .txt")
            data = model.import_txt_file(path)
            print('Данные успешно импортированы\n')
            view.show_data(data)
            logging.info("Успех!")
        if format == 2:
            logging.info("Выбран формат .csv")
            data = model.import_csv_file(path)
            print('Данные успешно импортированы\n')
            view.show_data(data)
            logging.info("Успех!")
    elif select == 2:
        logging.info("Выбран экспорт файла")
        format = view.import_export_menu()
        if format == 1:
            logging.info("Выбран формат .txt")
            data = model.import_csv_file('file.csv')
            model.export_txt(data)
            logging.info("Успех!")
        if format == 2:
            logging.info("Выбран формат .csv")
            data = model.import_txt_file('file.txt')
            model.export_csv(data)
            logging.info("Успех!")
