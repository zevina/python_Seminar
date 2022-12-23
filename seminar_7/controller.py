import view
import model
import logging

logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.INFO, encoding='utf-8')


def main_function():
    try:
        select = view.greeting()
        if select == 1:
            logging.info("Выбран режим калькулятор")
            example = view.get_math_example()
            result = model.calc(example)
            view.view_result(result)
            logging.info(f"Результат получен: {result}")
        elif select == 2:
            logging.info("Выбран режим конвертер")
            weight = view.get_weight()
            logging.info(f"Введено значение веса, {weight}")
            value = model.converter(weight)
            view.view_result(value)
            logging.info(f"Результат получен: {value} г")
    except Exception as e:
        logging.warning(f'Ошибка ввода данных - попробуйте ещё раз", {e}')