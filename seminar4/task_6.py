# 6. Дан текст: в первой строке задано число строк, далее идут сами строки.
# Выведите слово, которое в этом тексте встречается чаще всего.
# Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.
#
# Входные данные
# 1
# apple orange banana banana orange
#
# Выходные данные
# banana

user_str = 'apple orange banana banana orange'
sp = user_str.split()
sl = {}

for el in sp:
    sl[el] = sl.get(el, 0) + 1
print(sl)

sl = dict(sorted(sl.items()))
print(sl)

max_value = max(sl.values())

for key, value in sl:
    if value == max_value:
        print(key)
        break