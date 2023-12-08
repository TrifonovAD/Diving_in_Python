import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


# Введите ваше решение ниже

def check_multiplicity(amount):
    if amount % MULTIPLICITY == 0:
        return True
    else:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False


def deposit(amount):
    global bank_account, operations
    if check_multiplicity(amount):
        bank_account += amount
        operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')


def withdraw(amount: decimal.Decimal):
    global bank_account, operations
    comission: decimal.Decimal = amount * PERCENT_REMOVAL
    check_multiplicity(amount)
    if comission < MIN_REMOVAL:
        comission = MIN_REMOVAL
    if comission > MAX_REMOVAL:
        comission = MAX_REMOVAL
    withdraw_sum: decimal.Decimal = amount + comission
    if bank_account < comission + amount:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {withdraw_sum} у.е. На карте {bank_account} у.е.')
    else:
        if check_multiplicity(amount):
            bank_account -= (amount + comission)
            operations.append(
                f'Снятие с карты {amount} у.е. Процент за снятие {comission} у.е.. Итого {bank_account} у.е.')


def exit():
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        richness_summa: decimal.Decimal = bank_account * RICHNESS_PERCENT
        bank_account -= richness_summa
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT} в сумме {richness_summa} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')

deposit(173)
withdraw(21)
exit()

print(operations)