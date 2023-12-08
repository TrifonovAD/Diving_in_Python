# Задание №7 Пользователь вводит строку текста.
# Подсчитайте сколько раз встречается каждая буква в строке без использования метода count и с ним.
# Результат сохраните в словаре, где ключ — символ, а значение — частота встречи символа в строке.
# Обратите внимание на порядок ключей. Объясните почему они совпадают или не совпадают в ваших решениях.

user_data = input('Введите текст: ')

dict_count_char = {char: user_data.count(char) for char in set(user_data)}


print(dict_count_char)

dict_count_char_2 = {}

for char in user_data:
    dict_count_char_2[char] = dict_count_char_2.get(char, 0) + 1

print(dict_count_char_2)