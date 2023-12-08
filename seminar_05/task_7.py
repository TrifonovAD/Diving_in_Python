# Задание №7
# Создайте функцию-генератор.
# Функция генерирует N простых чисел, начиная с числа 2.
# Для проверки числа на простоту используйте правило:
# «число является простым, если делится нацело только на единицу и на себя».

def check_prime(number):
    if number % 2 == 0 and number != 2:
        return False
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
def generator(num):
    prime_num = 1
    while num:
        prime_num += 1
        if check_prime(prime_num):
            num -= 1
            yield prime_num


n = int(input("Введите число: "))
for number in generator(n):
    print(number)