# Задание №6
# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# Для вывода результата используйте «принт» без перехода на новую строку.


LOWER_LIMIT = 2
UPPER_LIMIT = 10
COLUMN = 4


my_gen_multiply = (f'{k:>2} * {j:>2} = {k * j:>2}\t' if k != i + COLUMN - 1 else \
                   f'{k:>2} * {j:>2} = {k * j:>2}\n' if j != UPPER_LIMIT else \
                   f'{k:>2} * {j:>2} = {k * j:>2}\n\n'
                   for i in (LOWER_LIMIT, COLUMN + LOWER_LIMIT) \
                   for j in range(LOWER_LIMIT, UPPER_LIMIT + 1) \
                   for k in range(i, i + COLUMN)
                   )

print(*my_gen_multiply, end='')