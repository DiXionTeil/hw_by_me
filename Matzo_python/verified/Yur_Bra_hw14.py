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
    def __init__(self, year_birth: int, name: str, sername: str):
        self.year_birth = year_birth
        self.age = date.today().year - year_birth
        self.name = name + ' ' + sername
        self.__friends = []
        print(f'Initialization person \033[1m\033[{random.randint(31, 36)}m{self.name}\033[0m')

    def know(self, another_person_object):
        self.__friends.append(another_person_object)

    def is_known(self, another_person_object):
        if another_person_object in self.__friends:
            return True
        return False


# ────────── * TESTING * ──────────

boris = Person(2000, 'Boris', 'Borisovich')
lolik = Person(1994, 'Lolik', 'Bess')
kira = Person(1978, 'Kira', "bojenova")
valentine = Person(-5063, 'Valentine', 'Dohrinicha let')
boris.know(lolik)
boris.know(kira)
kira.know(valentine)
print(boris.is_known(lolik))
print(valentine.is_known(kira))
print(lolik.is_known(boris))

# ─────────────────────────────────
