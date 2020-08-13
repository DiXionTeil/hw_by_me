"""
Реализовать класс Person, у которого должно быть два атрибута: age и name.
Также у него должен быть следующий набор методов:
    def know(self, another_person_object)
который позволяет добавить другого человека в список знакомых
(лист __friends (обязательно приватный атрибут)).


И метод
    def is_known(self, another_person_object)
который возвращает знакомы ли два человека (True/False)
"""
from datetime import date
import random

class Person:
    # классовые атрибуты
    count = 0  # индекс очередности добавления объектов в список всех контактов
    persons = {}  # список всех контактов
    __names = []

    # данный метот вызывается при создание обьекта и передает ему след. атрибуты:
    def __init__(self, year_birth: int, name: str, sername: str):  # атрибут age является ЧИСЛОМ, а name - строкой
        # определил атрибуты (метода)
        self.year_birth = year_birth  # год рождения
        self.age = date.today().year - year_birth  # возраст
        self.name = name + ' ' + sername
        self.__friends = []  # приватный атрибут
        print(f'Initialization person \033[1m\033[{random.randint(31,36)}m{self.name}\033[0m')

        Person.count += 1  # увеличивается при каждой нов. иниц-ции объекта
        Person.__names.append(self.name)  # добавляем имена
        Person.name_age = {self.name: self.age}  # подразумевается, что все имена будут уникальны
        Person.persons[Person.count] = Person.name_age  # список всех контактов

    @staticmethod
    def dict_persons():
        return Person.persons  # выводит список контактов

    # плюшка для того, чтобы растянуть дефис в консоле
    @staticmethod
    def len_names():
        return max(len(i) for i in Person.__names)

    def know(self, another_person_object):
        self.__friends.append(self)  # man_1 knows man_1 - знает
        self.__friends.append(another_person_object)  # man_1 knows man_2 - знаком

    def is_known(self, another_person_object):
        if another_person_object in self.__friends:
            return True
        return False


# ────────── * TESTING * ──────────

boris = Person(2000, 'Boris', 'Borisovich')
lolik = Person(1994, 'Lolik', 'Bess')
kira = Person(1978, 'Kira', "bojenova")
valentine = Person(-5063, 'Valentine', 'Dohrinicha let')
print('─' * (22 + Person.len_names()))
print(boris.name, boris.year_birth, boris.age)
print(valentine.age)
print('─' * (22 + Person.len_names()))
boris.know(lolik)
boris.know(kira)
kira.know(valentine)
print(boris.is_known(boris))
print(valentine.is_known(kira))
print(lolik.is_known(boris))
print('─' * (22 + Person.len_names()))
print(Person.dict_persons())

# ─────────────────────────────────
