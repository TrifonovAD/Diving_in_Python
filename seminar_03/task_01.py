# Задание №1 Вручную создайте список с целыми числами, которые повторяются.
# Получите новый список, который содержит уникальные (без повтора) элементы исходного списка.
# *Подготовьте два решения, короткое и длинное, которое
# не использует другие коллекции помимо списков.

my_list = [3, 6, 3, 65, 2, 23, 7, 12, 43, 97, 7, 2, 97]

new_list = list(set(my_list))
print(new_list)

new_list2 = []
for item in my_list:
    if item not in new_list2:
        new_list2.append(item)
print(new_list2)