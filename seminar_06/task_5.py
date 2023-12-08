# Задание №5
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

def storage_riddles() -> None:
    riddles = {'В поле лестница лежит, дом по лестнице бежит.': ['поезд'], \
               'Разноцветное коромысло над рекой повисло.': ['радуга'], \
               'Два конца, два кольца, посредине гвоздик.': ['ножницы']}
    for key, value in riddles.items():
        result = secrets(key, value)
        print(f'Угадал с {result} попытки.' if result != 0 else 'Не угадал.')

if __name__ == '__main__':
    storage_riddles()