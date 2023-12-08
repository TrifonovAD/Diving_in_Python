# Задание №4 Создайте вручную список с повторяющимися элементами.
# Удалите из него все элементы, которые встречаются дважды.

my_list = [2, 5, 6, 8, 3, 4, 4, 5, 6, 7, 9, 2, 5, 5]
COUNT_NUM = 2

for item in set(my_list):
    if my_list.count(item) == COUNT_NUM:
        for _ in range(COUNT_NUM):
            my_list.remove(item)

print(my_list)