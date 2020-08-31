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
import sys


class Hero:
    def __init__(self, name):
        self.name = name

    def hero_say(self, text: str):
        return f'{self.name} say:\n\"{text}\"'


class Some_heroes(Hero):
    pass


class Colobok(Hero):
    def mind_woke_up(self, name_of_mind):
        return Voice_of_reason(name_of_mind)


class Babka(Hero):
    def bake_colobok(self, name_colobok):
        return Colobok(name_colobok)


class Ded(Hero):
    pass


class Voice_of_reason(Hero):
    pass


class Fox(Hero):
    pass


class Tale:
    def __init__(self, babka, ded, fox):
        self.babka = babka
        self.ded = ded
        self.ded_ok = str(self.ded) + 'ok'
        self.fox = fox
        self.colobok, self.voice = None, None

    # 1st location, scene 1:
    def babkin_dom1(self):
        global dedok, babok
        dedok = Ded(self.ded)
        babok = Babka(self.babka)
        print(dedok.hero_say('We need to create a child, bab.'))
        time.sleep(1)
        print(babok.hero_say(f'F**k you, {self.ded_ok}. Let\'s do the sh*t!'))
        return babok, dedok

    # 1st location, scene 2:
    def babkin_dom2(self):
        global new_life_was_born, babka_and_ded, voice_of_reason, colobok
        self.colobok = 'Kolobok'
        new_life_was_born = babok.bake_colobok(self.colobok)
        print(dedok.hero_say('YES, YEEES!!! Wait, what?...'))
        babka_and_ded = Some_heroes(' and '.join([self.babka, self.ded]))
        time.sleep(2)
        print(babka_and_ded.hero_say('NANI?'))
        time.sleep(2)
        sys.stdout.write('I...')
        time.sleep(1)
        sys.stdout.write('AM...')
        time.sleep(1)
        sys.stdout.write('ALIVE!!!\n')
        time.sleep(1)
        print(new_life_was_born.hero_say(f'Hello, my name is {self.colobok}. Nice to meet you.'))
        self.voice = 'Voice of REASON'
        voice_of_reason = new_life_was_born.mind_woke_up(self.voice)
        time.sleep(2)
        print(voice_of_reason.hero_say('Run'))

    # game: TODO вызвать только ОДИН раз
    def game_with_fox(self, foxi):
        print(foxi.hero_say('We start to play to the game'))
        first_player_status, second_player_status = None, None
        count_of_win_1pl, count_of_win_2pl = 0, 0
        time.sleep(2)
        print('Fist question is...')
        first_question = input('What is My name?\n>')
        if first_question == self.fox:
            count_of_win_1pl += 1
            print(foxi.hero_say('Ph...ef...correct...'))
        else:
            count_of_win_1pl -= 1
            count_of_win_2pl += 1
            print(foxi.hero_say('Wrong!'))
        # testing
        # print(f'{count_of_win_1pl} and {count_of_win_2pl}')
        time.sleep(1)
        sys.stdout.write(foxi.hero_say('I chose number...'))
        time.sleep(2)
        sys.stdout.write('from 1 to 5!\n')
        random_number = random.randint(6, 10)
        second_question = input('>')
        if second_question == random_number:
            count_of_win_1pl += 1
            if count_of_win_1pl == 2:
                print(foxi.hero_say('Ph...ef...correct again'))
            else:
                print(foxi.hero_say('Ph...ef...correct...'))
        else:
            count_of_win_1pl -= 1
            count_of_win_2pl += 1
            if count_of_win_1pl == 0:
                print(foxi.hero_say('Wrong!'))
            else:
                print(foxi.hero_say('Ha-ha-ha...Wrong again!'))
        if count_of_win_1pl > 0:
            first_player_status = True
        else:
            first_player_status = False
        if count_of_win_2pl > 0:
            second_player_status = True
        else:
            second_player_status = False
        # testing
        # print(f'{count_of_win_1pl} and {count_of_win_2pl}\n
        # {first_player_status} and {second_player_status}')
        return [first_player_status, second_player_status]

    # 2nd location, scene 3:
    def forest(self, foxi):
        print(foxi.hero_say(f'I\'m {self.fox}. Let\'s play.'))
        game_by_fox = self.game_with_fox(foxi)
        if game_by_fox[1] is False and game_by_fox[0] is True:
            print(f'{self.colobok} stay alive')
        elif game_by_fox[1] is True:
            print(f'{self.colobok} is dead')

    def start(self):
        self.babkin_dom1()
        time.sleep(1)
        print('''
    Some time late...
        ''')
        time.sleep(1)
        self.babkin_dom2()
        time.sleep(1)
        print(f'{self.colobok} went away...')
        time.sleep(2)
        sys.stdout.write('''
    Some time late...''')
        time.sleep(2)
        sys.stdout.write('''in forest
            \n''')
        time.sleep(2)
        foxi = Fox(self.fox)
        self.forest(foxi)
        time.sleep(2)
        print(f'''
    \033[1m\033[31mThe end\033[0m?
        ''')


# ────────── * TESTING * ──────────

my_tail = Tale('Babka', 'Ded', 'Foxi')
my_tail.start()

# ─────────────────────────────────