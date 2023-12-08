# Задание №5 Напишите программу, которая решает квадратные уравнения даже если дискриминант отрицательный.
# Используйте комплексные числа для извлечения квадратного корня.

print("Решение квадратного уравнения ax^2 + bx + c = 0. Где a, b, c - целые числа.")

a: int = int(input("Введите a: "))
b: int = int(input("Введите b: "))
c: int = int(input("Введите c: "))

discriminant = b ** 2 - 4 * a * c

if discriminant == 0:
    x = -b / (2 * a)
    result: str = f'У уравнения один корень: {x=}'
elif discriminant > 0:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    result: str = f'У уравнения два корня:\n{x1=}\n{x2=}'
else:
    discriminant = complex(discriminant)
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    x1 = round(x1.real, 2) + round(x1.imag, 2) * 1j
    x2 = round(x2.real, 2) + round(x2.imag, 2) * 1j
    result: str = f'У уравнения два комплексных корня:\n{x1=}\n{x2=}'

print(result)
