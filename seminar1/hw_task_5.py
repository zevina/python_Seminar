# 5.	Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
#
# Пример:
# o	A (3,6); B (2,1) -> 5,09
# o	A (7,-5); B (1,-1) -> 7,21

x1, y1 = int(input('Введите координату Х для точки А: ')), int(input('Введите координату Y для точки А: '))
x2, y2 = int(input('Введите координату Х для точки B: ')), int(input('Введите координату Y для точки B: '))

d = str(round((((x2-x1) ** 2 + (y2-y1) ** 2) ** 0.5), 3))
print('Расстояние между точками: ', d[0:-1])