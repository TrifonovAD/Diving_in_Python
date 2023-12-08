# Задание №7 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

from sys import argv

def _is_leap(year: int) -> bool:
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0 #Проверка на високосный год

def valid(full_date: str) :
    day, month, year = (int(item) for item in full_date.split('.'))
    if not (0 < day < 32 and 0 < month < 13 and 0 < year < 10_000):
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2 and day > 29:
        return False
    if month == 2 and not _is_leap(year) and day == 29:
        return False
    return True

if __name__ == '__main__':
    date_to_prove = '29.02.2000'
    print(valid(date_to_prove))