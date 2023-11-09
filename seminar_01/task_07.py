# Задание №7
# Пользователь вводит число от 1 до 999. Используя операции с числами
# сообщите что введено: цифра, двузначное число или трёхзначное число.
# Для цифры верните её квадрат, например 5 - 25
# Для двузначного числа произведение цифр, например 30 - 0
# Для трёхзначного числа его зеркальное отображение, например 520 - 25
# Если число не из диапазона, запросите новое число
# Откажитесь от магических чисел
# В коде должны быть один input и один print
#

MIN_NUMBER = 1
MAX_NUMBER = 999
NUMBER_NON_RANGE = 0
TEN = 10
HUNDRED = 100

number = NUMBER_NON_RANGE
while number < MIN_NUMBER or number > MAX_NUMBER:
    number = int(input(f'Введите чилсло из диапазона от {MIN_NUMBER} до {MAX_NUMBER}: '))
if number < TEN:
    result = f'Число {number} - однозначное, его квадрат равен {number * number}'
elif number < HUNDRED:
    result = f'Число {number} - двухзначное, произведение его цифр {(number // TEN) * (number % TEN)}'
else:
    result = f'Число {number} - трехзначное, его зеркальное отображение {int(str(number)[::-1])}'

print(result)
