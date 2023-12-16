# Задание №3
# ✔ Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.
from pathlib import Path
from typing import TextIO


def read_line_from_begin(fd: TextIO) -> str:
    text_from_file = fd.readline()
    if not text_from_file:
        fd.seek(0)
        text_from_file = fd.readline()
    return text_from_file[:-1]


def convert_files(names: str | Path, numbers: str |Path, new_file: str | Path) -> None:
    with (
        open(names, 'r', encoding='utf-8') as f_names,
        open(numbers, 'r', encoding='utf-8') as f_numbers,
        open(new_file, 'w', encoding='utf-8') as new_f
    ):
        len_names = sum(1 for _ in f_names)
        len_numbers = sum(1 for _ in f_numbers)
        max_len = max(len_names, len_numbers)

        for item in range(max_len):
            name = read_line_from_begin(f_names)
            num_txt = read_line_from_begin(f_numbers)
            num_int, num_float = num_txt.split(' | ')
            mult_num = int(num_int) * float(num_float)
            if mult_num < 0:
                name = name.lower()
                mult_num = abs(mult_num)
            else:
                name = name.upper()
                mult_num = round(mult_num)
            new_f.write(f'{name} | {mult_num}\n')


if __name__ == '__main__':
    convert_files('names.txt', 'numbers.txt', 'result.txt')