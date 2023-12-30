# Задание №6
# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён.


from pathlib import Path
from random import randint, choices
from string import ascii_lowercase, digits


def create_files(extension: str, min_len_name: int = 6, max_len_name: int = 30,
                 min_file_size: int = 256, max_file_size: int = 4096,
                 count_files: int = 42, folder=None) -> None:
    for _ in range(count_files):
        filename = ''.join(choices(ascii_lowercase + digits + '_', k=randint(min_len_name, max_len_name + 1)))
        data = bytes(randint(0, 255) for _ in range(randint(min_file_size, max_file_size + 1)))
        with open(folder / f'{filename}.{extension}', 'wb') as f:
            f.write(data)


def files_generator(folder_name: str | Path, **kwargs) -> None:
    if isinstance(folder_name, str):
        folder_name = Path(folder_name)

    # Проверяем существует ли такая директория. Если нет, создаем ее
    if not folder_name.is_dir():
        folder_name.mkdir(parents=True)

    for extension, count in kwargs.items():
        create_files(extension, count_files=count, folder=folder_name)


if __name__ == '__main__':
    files_generator('test_folder', txt=1, jpg=2, doc=3, pdf=2)
