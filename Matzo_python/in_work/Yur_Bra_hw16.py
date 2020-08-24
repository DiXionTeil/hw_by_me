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