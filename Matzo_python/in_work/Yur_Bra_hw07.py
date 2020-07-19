import time


# 1st task
def get_season(number):
    if number in [1, 2, 12]:
        print('Зима')
    elif number in [3, 4, 5]:
        print('Весна')
    elif number in [6, 7, 8]:
        print('Лето')
    elif number in [9, 10, 11]:
        print('Осень')
    elif not number.isdigit():
        print('Не корректное значение')
    return number


# ────────── * TESTING * ──────────
# get_season(4)
#
# time.sleep(2)
#
# get_season('b')


# ─────────────────────────────────


# 2nd task
from collections import Counter


def converter(string, separator):
    count_list = []
    for word in string.split(separator):
        clear_list = ''
        for letter in word:
            if type(letter) == str:
                clear_list += letter.lower()

        count_list.append(clear_list)
    return print(Counter(count_list))


# ────────── * TESTING * ──────────

# my_str = input('String\n>')
# delimiter = input('delimiter\n>')
#
# converter(my_str, delimiter)

# ─────────────────────────────────

# 3d task
def get_rectangle_data(side):
    if not isinstance(side, (int, float)):
        print('Не корректное значение')
        return side
    print(f'Сторона квадрата =', side)
    square_Perimeter = side * 4
    square_Area = side ** 2
    square_Diagonal = side * 2 ** 0.5
    return print(f'Периметр квадрата = {square_Perimeter}\n'
                 f'Площать квадрата = {square_Area}\n'
                 f'Диагональ квадрата = {square_Diagonal}')


# ────────── * TESTING * ──────────
# get_rectangle_data(4)
# print('''
#
# ''')
#
# time.sleep(2)
#
# get_rectangle_data(2.35)
# print('''
#
# ''')
#
# time.sleep(2)
#
# get_rectangle_data('b')
#

# ─────────────────────────────────


