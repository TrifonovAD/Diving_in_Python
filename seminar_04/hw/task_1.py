# Преобразование ключей и значений словаря
# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример использования.
# На входе:
# params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
# print(params)
# На выходе:
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}


def key_params(**kwargs):
    result = {}
    for key, value in kwargs.items():
        if hashable(value) and value != None:
            result[value] = key
        else:
            result[str(value)] = key
    return result

def hashable(obj):
    try:
        hash(obj)
        return True
    except TypeError:
        return False

params = key_params(a = None, b = '', c = [], d = {})
print(params)

