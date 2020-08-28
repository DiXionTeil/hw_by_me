# 1st task:
"""
Реализовать класс Банкомат, у которого есть баланс. Банкомат может выдавать деньги и принимать платежи.
Банкомат не может уйти в минус и не может обрабатывать отрицательные сумму.
Что делать дома:
    - реализовать конвертацию c различных валют в гривну при добалении денег в банкомат и при снятии
"""
from dataclasses import dataclass


@dataclass
class Value:
    amount: float
    currency: str


class ATM:
    min_limit = 100
    max_limit = 3000
    bank_name = 'Mono'

    def __init__(self, amount):
        self.initial_amount = self._validate_amount(amount)
        self.currency = 'UAH'
        self.curr_map = {'USD': 27.8, 'EUR': 32.2}

    def _validate_amount(self, amount):
        if amount <= 0:  # Банкомат не может обрабатывать отрицательные сумму
            raise ValueError
        return amount

    def add_money(self, value, currency=None):
        self._validate_amount(value)
        if currency in self.curr_map.keys():
            self.currency = currency
            self.initial_amount += value * self.curr_map.get(currency)
        else:
            self.initial_amount += value

    def withdraw(self, amount):
        self._validate_amount(amount)
        if self.currency in self.curr_map.keys():
            amount = amount * self.curr_map.get(self.currency)
        if self.initial_amount < amount:
            raise ValueError('Not enough money')
        elif amount > self.max_limit:
            raise ValueError('Mush more than you might')
        elif amount < self.min_limit:
            raise ValueError('Must enter more')
        self.initial_amount -= amount
        # подсчитывает копейки, если таковы есть, и возвращает ошибку
        # if amount % 1 != 0:
        #     raise ValueError('Without cents')
        # или возвращает на счет банка
        #     self.initial_amount += amount % 1
        # return int(amount)  # не выдаем копейки
        return float(amount)


# ────────── * TESTING * ──────────

# atm = ATM(100000)
# atm.add_money(200, 'USD')
# print(atm.withdraw(5))
#
# atm2 = ATM(atm.initial_amount)
# atm2.add_money(10)
# print(atm2.withdraw(500.2))

# ─────────────────────────────────


# 2nd task:
"""
Нужно дописать основную линию сказки. Каждого героя реализовать классом с методами. 
Так же должен быть класс сказки (или функция), где происходит основное действие с героями
"""


# ___________KOLOBOK_______________
import random
import time


class Hero:
    def __init__(self, name):
        self.name = name

    def hero_say(self, text: str):
        return f'{self.name} say:\n\"{text}\"'


class Some_heroes(Hero):
    pass


class Colobok(Hero):
    pass


class Babka(Hero):
    def bake_colobok(self, name_colobok):
        return Colobok(name_colobok)


class Ded(Hero):
    pass


class Fox(Hero):
    pass


class Tale:
    def __init__(self, babka, ded):
        self.babka = babka
        self.ded = ded
        self.ded_ok = str(self.ded) + 'ok'
        self.colobok = None

    def babkin_dom1(self):
        global dedok, babok
        dedok = Ded(self.ded)
        babok = Babka(self.babka)
        print(dedok.hero_say('We need to create a child, bab.'))
        print(babok.hero_say(f'F**k you, {self.ded_ok}. Let\'s do the sh*t!'))
        return babok, dedok

    def babkin_dom2(self):
        global new_life_was_born, babka_and_ded
        self.colobok = 'Kolobok'
        new_life_was_born = babok.bake_colobok(self.colobok)
        print(dedok.hero_say('YES, YEEES!!! Wait, what?...'))
        time.sleep(2)
        babka_and_ded = Some_heroes(' and '.join([self.babka, self.ded]))
        print(babka_and_ded.hero_say('NANI?'))
        time.sleep(2)
        print('I...AM...ALIVE!!!')
        time.sleep(1)
        print(new_life_was_born.hero_say(f'Hello, my name is {self.colobok}. Nice to meet you.'))

    def start(self):
        self.babkin_dom1()
        time.sleep(1)
        print('''
        Some time late...
        ''')
        time.sleep(1)
        self.babkin_dom2()


my_tail = Tale('Babka', 'Ded')

my_tail.start()

























# ────────── * TESTING * ──────────



# ─────────────────────────────────