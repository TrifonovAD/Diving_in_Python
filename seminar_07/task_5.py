# Задание №5
# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.



from random import randint, choices
from string import ascii_lowercase, digits


def files_generator(**kwargs) -> None:
    for extension, count in kwargs.items():
        create_files(extension, count_files=count)



def create_files(extension: str, min_len_name: int=6, max_len_name: int=30,
                 min_file_size: int=256, max_file_size: int=4096, count_files: int=42) -> None:
    for _ in range(count_files):
        filename = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len_name, max_len_name + 1)))
        data = bytes(randint(0, 255) for _ in range(randint(min_file_size, max_file_size + 1)))
        with open(f'{filename}.{extension}', 'wb') as f:
            f.write(data)



if __name__ == '__main__':
    files_generator(txt=1, jpg=2, doc=3, pdf=2)