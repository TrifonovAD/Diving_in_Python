# Задание №4
# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


from random import randint, choices
from string import ascii_lowercase, digits


def create_files(extension: str, min_len_name: int=6, max_len_name: int=30,
                 min_file_size: int=256, max_file_size: int=4096, count_files: int=42) -> None:
    for _ in range(count_files):
        filename = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len_name, max_len_name + 1)))
        data = bytes(randint(0, 255) for _ in range(randint(min_file_size, max_file_size + 1)))
        with open(f'{filename}.{extension}', 'wb') as f:
            f.write(data)



if __name__ == '__main__':
    create_files('bin', 6, 12, 100, 10_000, 5)