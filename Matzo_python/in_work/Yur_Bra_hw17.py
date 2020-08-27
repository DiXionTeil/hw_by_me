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
        self.is_student = is_student
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

    # добавляет студента в n-ую группу: "студент может учиться в нескольких группах"
    def add_to_group(self, group_add):
        self.group_is = group_add.name_group
        self.is_student = True
        # group_add.students_list.append({self.personal_index: self.name})
        group_add.students_list.append({self.personal_index: [self.name, self.ave_score]})

    # переносит студента в n-ую группу: "студент намерян перевестись в другую группу"
    def from_group_to_group(self, group1, group2):
        for i in group1.students_list:
            if self.personal_index in i:
                group1.students_list.remove({self.personal_index: [self.name, self.ave_score]})
                self.group_is = group2.name_group
                self.is_student = True
                group2.students_list.append({self.personal_index: [self.name, self.ave_score]})

    # определяет статус окончания курсов, если студент уже учился:
    # "студент окончил курсы (группу 'n')"
    def finished_the_education(self):
        if all([self.is_student, self.group_is]):
            self.is_student = False

    # удаляет из группы студента
    def remove_from_group(self, student_remove):
        for i in student_remove.students_list:
            if self.personal_index in i:
                student_remove.students_list.remove({self.personal_index: [self.name, self.ave_score]})

    def __str__(self):
        print(f'Index:\t\t{self.personal_index}\nStudent:\t{self.name}\n'
              f'Age:\t\t{self.age}\n'
              f'Ave. score:\t{self.ave_score}')
        if self.group_is is None:
            return f'Status:\t\t{"Student" if self.is_student is True else "Not Student"}\n' \
                   f'──────────────────────'
        else:
            return f'Status:\t\t{"Student" if self.is_student is True else "Finished"}\n' \
                   f'Group:\t\t{self.group_is}\n' \
                   f'──────────────────────'


class Group:
    def __init__(self):
        self.name_group = self._random_literals
        self.students_list = []

    @property
    def _random_literals(self):
        name_gr = ''
        for i in range(3):
            name_gr += ''.join(random.sample(string.ascii_uppercase, 1))
        return name_gr

    # возвращает средний балл группы:
    #           * необходимо принтить
    def average_score(self):
        if self.students_list:
            counter_of_scores = 0
            for i in self.students_list:
                counter_of_scores += i.get(''.join(i.keys()))[1]
            return counter_of_scores

    def __str__(self):
        list_new_str = '\n'.join(map(str, self.students_list))  # принтит список элементов с каждой строки
        if self.students_list:
            return f'{self.name_group}:\n{list_new_str}'
        else:
            return f'{self.name_group}:\nList is None'


if __name__ == '__main__':
    a1 = Student('Borris', 19, 99.2, True)
    a2 = Student('Barbara', 19, 90, True)
    a3 = Student('Lenny', 20, 75, False)
    a4 = Student('Gregos', 16, 83.5, True)
    g1 = Group()
    g2 = Group()
    print(a2)
    print(a3)
    print(a4)
    print(a1)
    print(g1)
    print(g2)
    print('\n')
    a1.add_to_group(g1)
    a2.add_to_group(g1)
    a3.add_to_group(g1)
    a4.add_to_group(g1)
    print(a3)
    print('\n')
    print(g1)
    print(g2)
    print('\n')
    a2.add_to_group(g2)
    a3.from_group_to_group(g1, g2)
    print(a3)
    print(g2)
    print(g1)
    print('\n')
    a1.finished_the_education()
    print(a1)
    a1.remove_from_group(g1)
    print(g2)
    print(g2.average_score())
    print(g1)
    print(g1.average_score())
