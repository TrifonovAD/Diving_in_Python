# text = input()
# print(f'Тип: {type(text)}', f'Адрес в памяти: {id(text)}', f'Хэш: {hash(text)}', sep='\n')
#
#
# print(int('aaaaa', base=18))

text = input("Введите текст: ")
if text.isdigit():
    print(bin(int(text)), oct(int(text)), hex(int(text)), sep='\n')
else:
    if text.isascii():
        print('ASCII')
    else:
        print('Not ASCII')

