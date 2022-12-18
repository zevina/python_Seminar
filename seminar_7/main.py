# import logging
#
# # если хотим, чтобы логи выводились в консоль
# logging.basicConfig(level=logging.INFO)
#
# # если хотим, чтобы логи записывались в файл
# logging.basicConfig(filename='log.txt',
#                     filemode='a',
#                     format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.INFO)
#
# def main():
#     …
#     logging.info("Данные от пользователя получены")
#     …
#     logging.warning("Ошибка обработки данных")

from controller import main_function

main_function()