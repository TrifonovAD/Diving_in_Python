# Cписок повторяющихся элементов
# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов.
#
# Пример
# На входе:
# lst = [1, 1, 2, 2, 3, 3]
# На выходе:
# [1, 2, 3]

# lst = [1, 1, 2, 2, 3, 3]
lst = [1, 2, 3, 4, 5, 6]

result = []
if len(lst) != len(set(lst)):
    for num in set(lst):
        if lst.count(num) > 1:
            result.append(num)
print(result)
