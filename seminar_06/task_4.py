# Задание №4
# Создайте модуль с функцией внутри.
# Функция получает на вход загадку, список с возможными вариантами отгадок и количество попыток на угадывание.
# Программа возвращает номер попытки, с которой была отгадана загадка или ноль, если попытки исчерпаны.
# Добавьте в модуль с загадками функцию, которая хранит словарь списков.
# Ключ словаря - загадка, значение - список с отгадками.
# Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.

def secrets(riddle: str, answers: list[str], attempts: int=3):
    print(f'Угадай загадку за {attempts} попыток.\n{riddle}')
    for i in range(attempts):
        answer = input(f'Попытка №{i+1}. Введите ответ: ').lower()
        if answer in answers:
            return i+1
    return 0



if __name__ == '__main__':
    result = secrets('Зимой и летом одним цветом.', ['ель', 'елка', 'ёлка', 'сосна'])
    print(f'Угадал с {result} попытки.' if result != 0 else 'Не угадал.')