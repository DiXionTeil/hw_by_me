import random

cell = 2


def create_line(cell_var):
    return random.sample(range(1, cell_var ** 2 + 1), cell_var ** 2)
# print(create_line(cell))

# def mass_9_x_9():
#     array = []
#     for i in range(1, 10):
#         new_line = create_line(cell)
#         array.append(dict([('a' + str(i) + '1', int(new_line[0])),
#                            ('a' + str(i) + '2', int(new_line[1])),
#                            ('a' + str(i) + '3', int(new_line[2])),
#                            ('a' + str(i) + '4', int(new_line[3])),
#                            ('a' + str(i) + '5', int(new_line[4])),
#                            ('a' + str(i) + '6', int(new_line[5])),
#                            ('a' + str(i) + '7', int(new_line[6])),
#                            ('a' + str(i) + '8', int(new_line[7])),
#                            ('a' + str(i) + '9', int(new_line[8]))]))
#     return array
#
#
# for i in mass_9_x_9():
#     print(i)
def array_sudoku(cell_var):
    def dict_lines(cell_var, line):
        d = {}
        list_line = create_line(cell_var)
        for val in list_line:
            d.setdefault('a' + str(line) + '_' + str(list_line.index(val) + 1), val)
        return d

    array = []
    for line in range(1, cell_var ** 2 + 1):
        array.append(dict_lines(cell_var, line))
    return array


for i in array_sudoku(cell):
    print(i.values())
