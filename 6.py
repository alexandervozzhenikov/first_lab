import math
b = float(input("Введите катет = "))
a = float(input("Введите гипотенузу ="))
s = 0.5*a*b
c = math.sqrt(a**a-b**b)
print('Длина второго катета=',c,)
print('Площадь прямоугольного треугольника равна ',s,)