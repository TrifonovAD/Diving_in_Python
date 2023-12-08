# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
# Пример использования.
# На входе:
# file_path = "C:/Users/User/Documents/example.txt"
# На выходе:
# ('C:/Users/User/Documents/', 'example', '.txt')




# def get_file_info(file_path):
#     *path, rest = file_path.rsplit('/', 1)
#     if path:
#         path = str(*path) + '/'
#     else:
#         path = str(*path)
#     *name, ext = rest.rsplit('.', 1)
#     return (path, str(*name), '.' + ext)

# file_path = "C:/Users/User/Documents/example.txt"


def get_file_info(file_path):
    file_name = file_path.split("/")[-1]
    print(file_name)
    file_extension = file_name.split(".")[-1]
    path = file_path[:-len(file_name)]
    return (path, file_name[:-len(file_extension)-1], "." + file_extension)


file_path = "C:/Users/User/Documents/example.txt"
print(get_file_info(file_path))