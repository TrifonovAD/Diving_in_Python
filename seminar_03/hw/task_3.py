# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# В переменную backpack сохраните словарь {предмет:вес} с вещами в рюкзаке.
# В переменную result выведите список, содержащий все возможные варианты backpack. Напечатайте переменную result.
# *Верните все возможные варианты комплектации рюкзака.

from pprint import pprint
import itertools

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

backpacks = []

keys = list(items.keys())
for r in range(1, len(items)+1):
    for subset_keys in itertools.combinations(keys, r):
        subset_values = [items[key] for key in subset_keys]
        if sum(subset_values) <= max_weight:
            combination = dict(zip(subset_keys, subset_values))
            backpacks.append(combination)

pprint(backpacks)