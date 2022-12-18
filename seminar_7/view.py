def greeting():
    print('Hello! Выберете действие: 1 - калькулятор, 2 - конвертер')
    select = int(input())
    return select


def get_math_example():
    example = input('Введите выражение: ')
    return example


def view_result(result):
    print('Результат: ', result)


def get_weight():
    weight = input('Введите массу в кг: ')
    return weight
