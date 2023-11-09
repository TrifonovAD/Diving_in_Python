STAR = '*'
SPACE = ' '

rows = int(input("Сколько рядов у ёлки? "))

for i in range(rows):
    stars = STAR * (2*i + 1)
    spaces = SPACE * (rows - i - 1)
    print(f'{spaces}{stars}')
