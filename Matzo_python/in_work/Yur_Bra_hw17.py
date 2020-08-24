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
class Group:
    def __init__(self):
        pass


class Student:
    def __init__(self, name: str, age: int, ave_score: float, is_student=True):
        self.name = name
        self.age = age
        self.ave_score = ave_score
        self.is_student = is_student or False
        self.personal_index = self._index()

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

    def __str__(self):
        return f'Index:\t\t{self.personal_index}\nStudent:\t{self.name}\n' \
               f'Age:\t\t{self.age}\n' \
               f'Ave. score:\t{self.ave_score}\n' \
               f'Position:\t{"Student" if self.is_student == True else "Not Student"}\n' \
               f'──────────────────────'

a1 = Student('Borris', 19, 99.2, True)
a2 = Student('Barbarra', 19, 90, True)
a3 = Student('Lenny', 20, 75, True)
a4 = Student('Gregos', 16, 83.5, True)

print(a1)
print(a2)
print(a3)
print(a4)


