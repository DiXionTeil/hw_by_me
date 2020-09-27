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


def game(labyrinth_str):
    def transform_to_list(text):
        text_new = text.split('\n')
        text_finally = []
        for i in text_new:
            text_list = []
            for j in i:
                text_list.append(j)
            text_finally.append(text_list)
        return text_finally


    def painter(labyrinth):
        count = 0
        for line in labyrinth:
            line.append('#')
        labyrinth.append(labyrinth[-1])

        lists_new = []
        for line in labyrinth:
            list_new = []
            for column in range(len(line) - 1):
                if labyrinth.index(line) > 0 and labyrinth[labyrinth.index(line) - 1][column] == '#' and line[column + 1] == '#' and line[column - 1] == '#':
                    list_new.append('#')
                    if line[column] == '.':
                        count += 1
                elif line[column] == '.' and (line[column + 1] == '.' or labyrinth[labyrinth.index(line) + 1][column] == '.'):
                    list_new.append('.')
                else:
                    list_new.append('#')
            lists_new.append(list_new)
        del lists_new[-1]
        # print(lists_new)
        if count > 0:
            return painter(lists_new)
        return lists_new


    labyrinth = transform_to_list(labyrinth_str)
    labyrinth_true = painter(labyrinth)
    for _ in labyrinth_true:
        print(_)

    points_edge = []

    # проверка точек вхождения в верху лабиринта
    if labyrinth_true[0].count('.') > 0:
        points_edge.append(0)  # строка
        points_edge.append(labyrinth_true[0].index('.'))  # столбец
    if labyrinth_true[0].count('.') > 1:
        labyrinth_true[0].reverse()
        points_edge.append(0)  # строка
        points_edge.append(labyrinth_true[0].index('.'))  # столбец
        labyrinth_true[0].reverse()

    # проверка точек вхождения по сторонам лабиринта
    left_edge = []
    right_edge = []
    for i in labyrinth_true:
        left_edge.append(i[0])
        right_edge.append(i[-1])

    # слева лабиринта
    if left_edge.count('.') > 0:
        if '.' in left_edge:
            # print(left_edge)
            points_edge.append(left_edge.index('.'))
            points_edge.append(0)
    if left_edge.count('.') > 1:
        left_edge.reverse()
        points_edge.append(len(left_edge) - 1 - left_edge.index('.'))
        points_edge.append(0)

        # справа лабиринта
        if right_edge.count('.') > 0:
            if '.' in right_edge:
                # print(left_edge)
                points_edge.append(right_edge.index('.'))
                points_edge.append(0)
        if right_edge.count('.') > 1:
            right_edge.reverse()
            points_edge.append(len(right_edge) - 1 - right_edge.index('.'))
            points_edge.append(0)

    # проверка точек вхождения снизу лабиринта
    if labyrinth_true[-1].count('.') > 0:
        points_edge.append(len(labyrinth_true) - 1)  # строка
        points_edge.append(labyrinth_true[-1].index('.'))  # столбец
    if labyrinth_true[-1].count('.') > 1:
        labyrinth_true[-1].reverse()
        points_edge.append(len(labyrinth_true) - 1)  # строка
        points_edge.append(labyrinth_true[-1].index('.'))  # столбец
        labyrinth_true[-1].reverse()

    return f'Точка входа_1: {[points_edge[0], points_edge[1]]}\nТочка входа_2: {[points_edge[2], points_edge[3]]}'


if __name__ == "__main__":
    # условно, это строка, преобразованная из матрици:
    labyrinth_str_1 = '##########\n.........#\n######.###\n#......###\n' \
                    '#.####.###\n#........#\n##.#######\n##.##.####\n' \
                    '##......##\n#######.##'

    labyrinth_str_2 = '##########\n.......###\n######.###\n#......###\n' \
                      '#.####.###\n.......###\n##.#######\n##.#######\n' \
                      '##....####\n##########'

    labyrinth_str_3 = '######.###\n.......###\n######.###\n#......###\n' \
                      '#.####.###\n#......###\n##.#######\n##.#######\n' \
                      '##....####\n##########'

    print(game(labyrinth_str_3))

