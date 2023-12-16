# Функция группового переименования файлов
# Напишите функцию группового переименования файлов в папке test_folder под названием rename_files. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# f. Папка test_folder доступна из текущей директории


from os import listdir, rename


def rename_files(new_filename: str, num_digits: int, source_ext: str, target_ext: str,  name_range: [int, int]=None):
    file_list = listdir('test_folder')
    file_list = [file for file in file_list if file.endswith(source_ext)]
    file_list.sort()

    for num, file in enumerate(file_list, 1):
        if name_range is None:
            name_range = [0, 0]
        if name_range[1] > (len(file) - len(source_ext) - 1):
            name_range[1] = len(file) - len(source_ext) - 1

        # print([0, len(file) - len(source_ext) - 1])
        # print(file[name_range[0]: name_range[1]])

        new_name = f'{file[name_range[0]: name_range[1]]}{new_filename}{num:0{num_digits}}.{target_ext}'
        rename(f'test_folder/{file}', f'test_folder/{new_name}')


if __name__ == '__main__':
    rename_files(3, 'doc', 'docx', 'file', [0, 5])