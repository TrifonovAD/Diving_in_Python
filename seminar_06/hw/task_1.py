# Вы работаете над разработкой программы для проверки корректности даты, введенной пользователем.
# На вход будет подаваться дата в формате "день.месяц.год".
# Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.
# Ваша программа должна предоставить ответ "True" (дата корректна) или "False" (дата некорректна) в зависимости от результата проверки.


from sys import argv

def _is_leap(year: int) -> bool:
    return not (year % 4 != 0 or (year % 100 == 0 and year % 400 != 0)) #Проверка на високосный год

def valid(full_date: str) :
    date, month, year = (int(item) for item in full_date.split('.'))
    if year < 1 or year > 9999 or month < 1 or month > 12 or date < 1 or date > 31:
        return False
    if month in (4, 6, 9, 11) and date > 30:
        return False
    if month == 2 and _is_leap(year) and date > 29:
        return False
    if month == 2 and not _is_leap(year) and date > 28:
        return False
    return True


date_to_prove = '30.2.2023'
if len(argv) > 1:
    print(valid(argv[1]))
else:
    print(valid(date_to_prove))


