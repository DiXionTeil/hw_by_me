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

    enter_points_1 = []  # точка входа
    enter_points_2 = []  # точка выхода

    # проверка точек вхождения в верху лабиринта
    for i in labyrinth_true[0]:
        if '.' in labyrinth_true[0]:
            enter_points_1.append(0)  # строка
            enter_points_1.append(labyrinth_true[0].index('.'))  # столбец
        if labyrinth_true[0].count('.') > 1:
            labyrinth_true[0].reverse()
            if '.' in labyrinth_true[0]:
                enter_points_2.append(0)  # строка
                enter_points_2.append(labyrinth_true[0].index('.'))  # столбец
            labyrinth_true[0].reverse()

    # проверка точек вхождения по сторонам лабиринта
    for i in labyrinth_true:
        # слева лабиринта
        if '.' in labyrinth_true[labyrinth_true.index(i)][0]:
            if not enter_points_1:  # если точка входа не найдена ранее
                enter_points_1.append(labyrinth_true.index(i))
                enter_points_1.append(i.index('.'))
            elif enter_points_1 and not enter_points_2:  # если точка входа уже известна
                enter_points_2.append(labyrinth_true.index(i))
                enter_points_2.append(i.index('.'))
        # справа лабиринта
        if '.' in labyrinth_true[labyrinth_true.index(i)][-1]:
            if not enter_points_1:  # если точка входа не найдена ранее
                enter_points_1.append(labyrinth_true.index(i))
                enter_points_1.append(i.index('.'))
            elif enter_points_1 and not enter_points_2:  # если точка входа уже известна
                enter_points_2.append(labyrinth_true.index(i))
                enter_points_2.append(i.index('.'))

    # проверка точек вхождения снизу лабиринта
    for i in labyrinth_true[-1]:
        if '.' in labyrinth_true[-1]:
            if not enter_points_1:
                enter_points_1.append(len(labyrinth_true))  # строка
                enter_points_1.append(labyrinth_true[-1].index('.'))  # столбец
            elif enter_points_1 and not enter_points_2:
                enter_points_2.append(len(labyrinth_true))  # строка
                enter_points_2.append(labyrinth_true[-1].index('.'))  # столбец
        if labyrinth_true[-1].count('.') > 1 and not enter_points_2:
            labyrinth_true[-1].reverse()
            if '.' in labyrinth_true[-1]:
                enter_points_2.append(len(labyrinth_true))  # строка
                enter_points_2.append(labyrinth_true[-1].index('.'))  # столбец
            labyrinth_true[-1].reverse()
    return f'Точка входа: {enter_points_1}\nТочка выхода: {enter_points_2}'


print(game(labyrinth_str))

