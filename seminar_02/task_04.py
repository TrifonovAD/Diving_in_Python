# Задание №4 Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# Диаметр не превышает 1000 у.е.
# Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
from decimal import Decimal
from decimal import getcontext

PI = Decimal(math.pi)
ZERO = Decimal(0)
MAX_DIAMETER = Decimal(1000)


getcontext().prec = 50
diameter = ZERO

while not ZERO < diameter <= MAX_DIAMETER:
    diameter = Decimal(input('Введите диаметр окружности: '))

area_circle = PI * ((diameter / 2) ** 2)
length_circle = PI * diameter

print(f'Площадь круга: {area_circle}\nДлина окружности: {length_circle}')


