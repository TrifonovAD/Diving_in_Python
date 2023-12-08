# Задание №3 Пользователь вводит данные. Сделайте проверку данных и преобразуйте если возможно в один из вариантов ниже:
# 1. Целое положительное число
# 2. Вещественное положительное или отрицательное число
# 3. Строку в нижнем регистре, если в строке есть хотя бы одна заглавная буква
# 4. Строку в верхнем регистре в остальных случаях

user_data = input('Введите данные: ')

if user_data.isdigit():
    result = int(user_data)
elif user_data.replace('.', '', 1).replace('-', '', 1).isdigit() \
        and user_data[1:].count('-') == 0 and user_data.count('.') != 0:
    result = float(user_data)
elif not user_data.islower():
    result = user_data.lower()
else:
    result = user_data.upper()

print(result, type(result))
