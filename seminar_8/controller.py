import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO,
                    encoding='UTF-8')


def main():
    select = view.show_menu()
    if select == 1:
        logging.info('Выбран пункт меню: 1')
        path = view.path_file()
        employees = model.import_file(path)
        view.show_employees(employees)
        logging.info('Отлично сработано!')
    elif select == 2:
        logging.info('Выбран пункт меню: 2')
        data = view.add_employees()
        model.add_employees_to_list(data)
        logging.info('Отлично сработано!')
    elif select == 3:
        logging.info('Выбран пункт меню: 3')
        path = view.path_file()
        employees = model.import_file(path)
        view.show_employees(employees)
        change, string = view.change_employees()
        model.update_employees(change, string)
        logging.info('Отлично сработано!')
    elif select == 4:
        logging.info('Выбран пункт меню: 4')
        path = view.path_file()
        employees = model.import_file(path)
        view.show_employees(employees)
        number = view.delete()
        model.delete(number)
        logging.info('Отлично сработано!')
    elif select == 5:
        logging.info('Выбран пункт меню: 5')
        path = view.path_file()
        employees = model.import_file(path)
        model.export_csv(employees)
        logging.info('Отлично сработано!')

