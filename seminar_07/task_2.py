# Задание №2
# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.

from pathlib import Path
import random

VOWELS = 'eyuioa'
CONSONANTS = 'qwrtpsdfghjklzxcvbnm'
MIN_LEN_NAME = 4
MAX_LEN_NAME = 7

def fill_file_names(filename: str | Path, quantity_names: int) -> None:
    with open(filename, 'w', encoding='utf-8') as file_names:
        while quantity_names > 0:
            name_length = random.randint(MIN_LEN_NAME, MAX_LEN_NAME + 1)
            name = ''.join(random.choice(VOWELS+CONSONANTS) for _ in range(name_length))
            if any(char in VOWELS for char in name):
                file_names.write(f'{name.capitalize()}\n')
                quantity_names -= 1

fill_file_names('names.txt', 15)