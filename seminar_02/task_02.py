# Задание №2. Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок.
# Для каждого элемента в цикле выведите:
# порядковый номер начиная с единицы
# значение
# адрес в памяти
# размер в памяти
# хэш объекта
# результат проверки на целое число только если он положительный
# результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys

data = [45, 3.14, 'Hello world!', 38, 21, 'Anna', True, 2 ** 16, 'Hello world!', '423', 'Привет, мир!', 1, 9 * 5]

for i, el in enumerate(data, start=1):
    check_int = 'Объект является целым числом' if isinstance(el, int) else ''
    check_str = 'Объект является строкой' if isinstance(el, str) else ''
    print(f'{i}. data[{i-1}] = {el}')
    print(f'Адрес в памяти: {id(el)}. Размер в памяти: {sys.getsizeof(el)}. Хэш: {hash(el)}. {check_int}{check_str}')


