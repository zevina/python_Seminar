# 4. Преобразовать набор списков (используя функцию zip)
#
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
#
# в другой набор
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
#
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
salary = [111, 222, 333]

res = list(zip(users, ids, salary))
print(res)

# res_2 = list(zip(res[0], res[1], res[2]))
res_2 = list(zip(*res))
print(res_2)

