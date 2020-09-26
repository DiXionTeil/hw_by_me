'''
##########
.........#
######.###
#......###
#.####.###
#........#
##.#######
##.##.####
##......##
#######.##
'''
'''
Написать фун-цию, которая возвращает начало
и конец лабиринта (координаты: [строка, столбец]).
ВАЖНО: массив размерности N на N!
'''

# условно, это строка, преобразованная из массива:
labyrinth_str = '##########\n.........#\n######.###\n#......###\n' \
                '#.####.###\n#........#\n##.#######\n##.##.####\n' \
                '##......##\n#######.##'

labyrinth_str_2 = '..##.\n#..#.\n##..#\n#.#.#\n#.#.#'
'''
. . # # .
# . . # .
# # . . #
# . # . #
# . # . #
'''

labyrinth_str_3 = '..#\n#.#\n.#.'
'''
. . #
# . #
. # .
'''


def transform_to_list_to_binary(text, symbol_1: str, symbol_2: str):
    text = text.replace(symbol_1, '1')
    text = text.replace(symbol_2, '0')
    text_new = text.split('\n')
    text_finally = []
    for i in text_new:
        text_list = []
        for j in i:
            text_list.append(j)
        text_finally.append(text_list)
    return text_finally


# def labyrinth_task(labyrinth):
#     for line in range(len(labyrinth)):
#         for column in range(len(labyrinth[line])):
#             if labyrinth[line][column] == '.' and (
#                     labyrinth[line][column + 1] == '.' or labyrinth[line + 1][column] == '.'):
#                 pass
#             else:
#                 print(labyrinth[line][column])
#         break
#     return 0


# for i in labyrinth_task(labyrinth):
#     print(i)

# print(labyrinth_task(labyrinth_str))


labyrinth = transform_to_list_to_binary(labyrinth_str_3, '.', '#')

list_0 = []
for i in labyrinth:
    list_0.append(list(1 if i[j] == '1' and i[j + 1] == '1' else 0 for j in range(len(i)-1)))

for i in list_0:
    print(i)
