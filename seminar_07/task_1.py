# Задание №1
# Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# Первое число int, второе - float разделены вертикальной чертой.
# Минимальное число - -1000, максимальное - +1000.
# Количество строк и имя файла передаются как аргументы функции.


import random
from pathlib import Path

MINIMUM = -1000
MAXIMUM = 1000

def fill_file_numbers(filename: str | Path, quantity_rows: int) -> None:
    with open(filename, 'w', encoding='utf-8') as file:
        for _ in range(quantity_rows):
            int_num = random.randint(MINIMUM, MAXIMUM + 1)
            float_num = random.uniform(MINIMUM, MAXIMUM + 1)
            file.write(f'{int_num} | {float_num}\n')
    return None

if __name__ == '__main__':
    fill_file_numbers('numbers.txt', 10)
