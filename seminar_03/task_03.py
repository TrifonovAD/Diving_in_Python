# Задание №3
# Создайте вручную кортеж содержащий элементы разных типов.
# Получите из него словарь списков, где: ключ — тип элемента, значение — список элементов данного типа.

# my_tuple = (23, -12.34, 'Hello world!', [1, 2, 3], 45, 98, 'Alex', [5, 6, 7])
my_tuple = (42, 73, 3.14, 'Hello world!', None, True, 'Text', 100500.2, False)

my_dict = {}

# Вариант 1.
# for item in my_tuple:
#     data_type = type(item).__name__
#     if data_type not in my_dict:
#         my_dict[data_type] = [item]
#     else:
#         my_dict[data_type].append(item)

# Вариант 2.

for item in my_tuple:
    data_type = type(item).__name__
    key = my_dict.setdefault(data_type, [])
    key.append(item)

print(my_dict)