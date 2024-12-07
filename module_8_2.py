from typing import Tuple, Any


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for i in numbers:
        try:
            result = result + i
        except TypeError:
            incorrect_data += 1
    res = (result, incorrect_data)
    return res

def calculate_average(numbers):
    try:
        num_l = len(numbers)
        re = personal_sum(numbers)
    except TypeError:
        return "В numbers записан некорректный тип данных"
    try:
        sr = re[0] / (num_l - re[1])
    except ZeroDivisionError:
        return 0
    return sr

# co = ['fd','ff',1, 3, 4, 'zcx','fff', 'zxczc']
# print(personal_sum(co))
# print(calculate_average(co))

print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать

