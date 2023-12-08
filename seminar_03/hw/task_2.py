# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.
# Пример
# На входе:
# text = 'Hello world. Hello Python. Hello again.'
#
# На выходе:
# [('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
text = "Hello world. Hello Python. Hello again."

text = text.lower()

for char in text:
    if not char.isalpha():
        text = text.replace(char, ' ')

word_list = text.split()

word_counts = {}

for word in word_list:
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

top_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]

print(top_words)