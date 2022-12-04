# 5.	Вам дан словарь, состоящий из пар слов. Каждое слово является синонимом к парному ему слову. Все слова в словаре различны.
# Для слова из словаря, записанного в последней строке, определите его синоним.
#
# Входные данные
# 3
# Hello Hi
# Bye Goodbye
# List Array
# Goodbye
#
# Выходные данные
# Bye

sl = {}
sl['Hello'] = 'Hi'
sl['Bye'] = 'Goodbye'
sl['List'] = 'Array'
print(sl)

user_word = input('Введите слово, а я дам синоним к нему: ')

for key, value in sl.items():
    if user_word == key:
        print(f'Синоним: {value}')
    elif user_word == value:
        print(f'Синоним: {key}')