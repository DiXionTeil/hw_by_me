import time


# 1st task
def get_season(number):
    monthes = ['Зима', 'Весна', 'Лето', 'Осень']
    if number in [1, 2, 12]:
        return f'{monthes[0]}'
    elif number in [3, 4, 5]:
        return f'{monthes[1]}'
    elif number in [6, 7, 8]:
        return f'{monthes[2]}'
    elif number in [9, 10, 11]:
        return f'{monthes[3]}'
    elif not number.isdigit():
        return False
    return number


# ────────── * TESTING * ──────────
# print(get_season(4))
#
# time.sleep(2)
#
# print(get_season('b'))


# ─────────────────────────────────


# 2nd task, 1st METHOD:
from collections import Counter


def converter_1(string, separator):
    return Counter(string.split(separator))


# ────────── * TESTING * ──────────

# my_str = input('String\n>')  # 'football, foot, summer, sum, ball, football'
# delimiter = input('delimiter\n>')  # ', '
#
# print(converter_1(my_str, delimiter))

# ─────────────────────────────────


# 2nd task, 2nd METHOD:
def converter_2(string, separator):
    res = {}
    temp_list = string.split(separator)
    for i in temp_list:
        res[i] = temp_list.count(i)
    return res


# ────────── * TESTING * ──────────

# my_str = input('String\n>')  # 'football, foot, summer, sum, ball, football'
# delimiter = input('delimiter\n>')  # ', '
#
# print(converter_2(my_str, delimiter))

# ─────────────────────────────────


# 2nd task, 3d METHOD:
def converter_3(string, separator):
    res = {}
    temp_list = [string.strip() for string in string.split(separator)]
    for i in temp_list:
        res[i] = temp_list.count(i)
    return res


# ────────── * TESTING * ──────────

# my_str = input('String\n>')  # 'football, foot, summer, sum, ball, football'
# delimiter = input('delimiter\n>')  # ',' without SPACE
#
# print(converter_3(my_str, delimiter))


# ─────────────────────────────────

# 2nd task, 4th METHOD:
def converter_4(string, separator):
    temp_list = [string.strip() for string in string.split(separator)]
    res_dict = dict.fromkeys(temp_list, 0)
    for i in temp_list:
        res_dict[i] +=1
    return res_dict


# ────────── * TESTING * ──────────

# my_str = input('String\n>')  # 'football, foot, summer, sum, ball, football'
# delimiter = input('delimiter\n>')  # ',' without SPACE
#
# print(converter_4(my_str, delimiter))


# ─────────────────────────────────


# 2nd task, 5th METHOD:
def converter_5(string, separator):
    temp_list = [string.strip() for string in string.split(separator)]
    res_dict = {i: temp_list.count(i) for i in temp_list}
    return res_dict


# ────────── * TESTING * ──────────

# my_str = input('String\n>')  # 'football, foot, summer, sum, ball, football'
# delimiter = input('delimiter\n>')  # ',' without SPACE
#
# print(converter_5(my_str, delimiter))


# ─────────────────────────────────


# 2nd task, 6th METHOD:
def converter_6(string, separator):
    res = {}
    temp_list = [string.strip() for string in string.split(separator)]
    for word in temp_list:
        if word not in res.keys():
            res[word] = 1
        else:
            res[word] += 1
    return res


# ────────── * TESTING * ──────────

# my_str = input('String\n>')  # 'football, foot, summer, sum, ball, football'
# delimiter = input('delimiter\n>')   # ',' without SPACE
#
# print(converter_6(my_str, delimiter))


# ─────────────────────────────────


# 3d task
def get_rectangle_data(side):
    if not isinstance(side, (int, float)):
        return side
    print(f'Сторона квадрата =', side)
    square_Perimeter = side * 4
    square_Area = side ** 2
    square_Diagonal = side * 2 ** 0.5
    return f'Периметр квадрата = {square_Perimeter}\n' \
           f'Площать квадрата = {square_Area}\n' \
           f'Диагональ квадрата = {square_Diagonal}'

# ────────── * TESTING * ──────────
# print(get_rectangle_data(4))
# print('''''')
#
# time.sleep(2)
#
# print(get_rectangle_data(2.35))
# print('''''')
#
# time.sleep(2)
#
# print(get_rectangle_data('b'))


# ─────────────────────────────────
