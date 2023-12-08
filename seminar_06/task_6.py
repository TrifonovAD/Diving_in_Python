# Задание №6 Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.


def secrets(riddle: str, answers: list[str], attempts: int=3):
    print(f'Угадай загадку за {attempts} попыток.\n{riddle}')
    for i in range(attempts):
        answer = input(f'Попытка №{i+1}. Введите ответ: ').lower()
        if answer in answers:
            return i+1
    return 0


def storage_riddles() -> None:
    riddles = {'В поле лестница лежит, дом по лестнице бежит.': ['поезд'], \
               'Разноцветное коромысло над рекой повисло.': ['радуга'], \
               'Два конца, два кольца, посредине гвоздик.': ['ножницы']}
    for key, value in riddles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки.' if result != 0 else 'Не угадал.')
        save_answer_num(key, result)


def save_answer_num(riddle: str, attempt: int) -> None:
    _data.update({riddle: attempt})


def print_result() -> None:
    result = (f'Загадку "{key}" угадали с {value} попытки.' if value > 0 \
              else f'Загадку "{key}" не угадали.' \
              for key, value in _data.items())
    print(*result, sep='\n')

if __name__ == '__main__':
    _data = {}
    storage_riddles()
    print_result()