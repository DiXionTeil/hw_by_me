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
# labyrinth_str = '##########\n.........#\n######.###\n#......###\n' \
#                 '#.####.###\n#........#\n##.#######\n##.##.####\n' \
#                 '##......##\n#######.##'

# labyrinth_str = '..##.\n#..#.\n##..#\n#.#.#\n#.#.#'

labyrinth_str = '..#\n#.#\n.#.'

labyrinth_list = labyrinth_str.split('\n')
labyrinth = []
for i in labyrinth_list:
    list_of_lists = []
    for j in i:
        list_of_lists.append(j)
    labyrinth.append(list_of_lists)
# print(labyrinth)


def labyrinth_task(labyrinth):
    for line in range(len(labyrinth)):
        for column in range(len(labyrinth[line])):
            if labyrinth[line][column] == '.' and (labyrinth[line][column + 1] == '.' or labyrinth[line + 1][column] == '.'):
                pass
            else:
                print(labyrinth[line][column])
        break
    return 0


# for i in labyrinth_task(labyrinth):
#     print(i)

# print(labyrinth_task(labyrinth_str))





l=[1, 1, 0, 1]
l1 = list(0 if l[i] > l[i+1] or l[i] == 0 else 1 for i in range(len(l)-1))


labyrinth_str = [[1, 1, 0], [0, 1, 0], [1, 0, 1]]

list_0 = []
for i in labyrinth_str:
    list_0.append(list(1 if i[j] == 1 and i[j+1] == 1 else 0 for j in range(len(i)-1)))

for i in list_0:
    print(i)