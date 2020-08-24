"""
 Создать класс, описывающий группу студентов - `Group`. Данный класс хранит студентов в виде списка объектов
 `Student` также реализованного в виде соответствующего класса.
В классах реализовать необходимый набор атрибутов (Например класс `Student` должен иметь атрибуты `name`, `age`,
`grades`), а так же необходимый набор методов экземпляра для работы с этими экземплярами.

Задание напоминает ТУДУ лист))
Методы студента и группы придумать любые (штуки по 4-5) в классах.
К примеру:
    - студент может покинуть группу
    - перейти в другую
"""
import random, string


class Student:
    def __init__(self, name: str, age: int, ave_score: float, is_student=True, group=None):
        self.name = name
        self.age = age
        self.ave_score = ave_score
        self.is_student = is_student or False
        self.personal_index = self._index()
        self.group_is = group

    def _index(self, __index_list=[]):
        while True:
            if not __index_list:
                index = 0
            else:
                index = int(__index_list[-1])
            index = str(index + 1).rjust(7 if len(str(index)) < 7 else 10, '0')
            if index in __index_list:
                continue
            else:
                __index_list.append(index)
                return index

    def add_to_group(self, Group):
        self.group_is = Group.name_group
        Group.students.append({self.personal_index: self.name})

    def __str__(self):
        if self.group_is is None:
            return f'Index:\t\t{self.personal_index}\nStudent:\t{self.name}\n' \
                   f'Age:\t\t{self.age}\n' \
                   f'Ave. score:\t{self.ave_score}\n' \
                   f'Position:\t{"Student" if self.is_student == True else "Not Student"}\n' \
                   f'──────────────────────'
        else:
            return f'Index:\t\t{self.personal_index}\nStudent:\t{self.name}\n' \
                   f'Age:\t\t{self.age}\n' \
                   f'Ave. score:\t{self.ave_score}\n' \
                   f'Position:\t{"Student" if self.is_student == True else "Not Student"}\n' \
                   f'Group:\t\t{self.group_is}\n' \
                   f'──────────────────────'


class Group:
    students = []

    def __init__(self):
        self.name_group = self._random_literals
        self.students_list = self.students

    @property
    def _random_literals(self):
        name_gr = ''
        for i in range(3):
            name_gr += ''.join(random.sample(string.ascii_uppercase, 1))
        return name_gr

    def __str__(self):
        return f'{self.name_group}:\n{self.students_list}'

if __name__ == '__main__':
    a1 = Student('Borris', 19, 99.2, True)
    a2 = Student('Barbara', 19, 90, True)
    a3 = Student('Lenny', 20, 75, False)
    a4 = Student('Gregos', 16, 83.5, True)
    g1 = Group()
    print(a2)
    print(a3)
    print(a4)
    print(a1)
    print(g1)
    print('')
    a1.add_to_group(g1)
    a2.add_to_group(g1)
    a3.add_to_group(g1)
    a4.add_to_group(g1)
    print(a3)
    print('')
    print(g1)

