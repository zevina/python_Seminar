# 9.	Для каждого слова исходного текста выведите одно целое число — номер вхождения этого слова в текст.
# Числа выведите через пробел. Количество чисел должно совпадать с количеством слов в исходном тексте.
#
# Входные данные
# Раз раз раз как меня слышно Повторяю раз раз раз Повторяю
#
# Выходные данные
# 1 1 2 1 1 1 1 3 4 5 2
#
TODO: user_str = input('Введите сообщение: ').split()
data_words = set(user_str)

phrase_words = {}
for word in user_str:
    phrase_words[word] = 0

# count = 0
# for word in user_str:
#     if word in words:

print(data_words)
print(phrase_words)
