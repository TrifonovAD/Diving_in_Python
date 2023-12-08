# Задание №6 Напишите программу банкомат.
# Начальная сумма равна нулю
# Допустимые действия: пополнить, снять, выйти
# Сумма пополнения и снятия кратны 50 у.е.
# Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# После каждой третей операции пополнения или снятия начисляются проценты - 3%
# Нельзя снять больше, чем на счёте
# При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# Любое действие выводит сумму денег

from decimal import Decimal

CMD_DEPOSIT = "п"
CMD_WITHDRAWAL = "с"
CMD_EXIT = "в"
MULTIPLICITY = 50
PERCENT_WITHDRAWAL = Decimal(15)/Decimal(1000)
MIN_WITHDRAWAL_FEE = 30
MAX_WITHDRAWAL_FEE = 600
COUNTER_OPERATION = 3
PERCENT_DEPOSIT = Decimal(3)/Decimal(100)
RICHNESS = 5_000_000
PERCENT_RICHNESS = Decimal(10)/Decimal(100)

user_bank_account = 0
user_counter_operation = 0
command = ''

while command != CMD_EXIT:
    command = input(f'Пополнить - {CMD_DEPOSIT}. Снять - {CMD_WITHDRAWAL}. Выйти - {CMD_EXIT}. ').lower()

    if command not in (CMD_EXIT, CMD_WITHDRAWAL, CMD_DEPOSIT):
        print('Неверная комманда!')
        continue

    if command == CMD_EXIT:
        print(f'Ваш баланс: {user_bank_account}')
        print('Работа завершена.')
        break

    if user_bank_account > RICHNESS:
        user_bank_account -= user_bank_account * PERCENT_RICHNESS

    elif command == CMD_DEPOSIT:
        pass
