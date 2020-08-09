"""
ITEMS       3       2       2 + XXX
------------------------------------
XXX         100     10      100
A           90      9       18
B           80      8       16
C           70      7       14
D           60      6       12
E           50      5       10
F           40      4       8
G           30      3       6
H           20      2       4
I           10      1       2
"""
import time, sys, random

pay_cash = 2
player_coins = 20
enter_coins = player_coins
symbols = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "XXX"]
chance = [10, 20, 30, 40, 50, 60, 70, 80, 90, 5]
value = {
    'XXX': 10,
    'A': 9,
    'B': 8,
    'C': 7,
    'D': 6,
    'E': 5,
    'F': 4,
    'G': 3,
    'H': 2,
    'I': 1
}
res = []


def play_uh(player_coins, pay_cash):
    question = input('Do you want to play [yes/no]:\n>')
    while not (question == 'yes' or question == 'no' or question == 'i have'):
        question = input('[yes/no]\n>')
    else:
        if question == 'no':
            print(f'You have \033[1m\033[35m{player_coins}\033[0m coins')
            exit(0)
        elif question == 'yes':
            game(enter_coins, player_coins, pay_cash, chance)
        elif question == 'i have':
            print(f'\033[1m\033[35m{player_coins}\033[0m coins')
            return play_uh(player_coins, pay_cash), player_coins


def random_chance(chance):
    return random.choices(symbols, weights=chance)


def game(enter_coins, player_coins, pay_cash, chance):
    result = 0

    if (player_coins - pay_cash) <= 0:
        print('You don\'t have enough coins')
        exit(0)
    player_coins -= pay_cash

    if (enter_coins * 1.5) < player_coins:
        chance = [2, 10, 15, 30, 30, 30, 30, 80, 100, 1]

    # 1st method: we have 3 wheels:
    for i in range(3):
        res.append(random_chance(chance))

    if res[0] == res[1] == res[2]:
        result = value[res[1][0]] * 10
    elif res[0] == res[1] and res[2][0] == symbols[-1]:
        result = value[res[1][0]] * 2
    elif res[0][0] == symbols[-1] and res[1] == res[2]:
        result = value[res[1][0]] * 2
    elif res[0] == res[1] or res[1] == res[2]:
        result = value[res[1][0]]
    # ─────────────────────────────

    # 2d method: we have n wheels:
    # in developing
    # ─────────────────────────────

    player_coins += result
    sys.stdout.write(f' {res[0]}')
    sys.stdout.flush()
    time.sleep(.8)
    sys.stdout.write(f' {res[1]}')
    sys.stdout.flush()
    time.sleep(.8)
    sys.stdout.write(f' {res[2]}')
    sys.stdout.flush()
    time.sleep(.8)
    sys.stdout.write('\n')
    # ─────TESTING───────
    # print(player_coins)
    # print(chance)
    # ───────────────────
    if result > 0:
        print(f'You\'re win \033[1m\033[3m{result} points\033[0m')
    res.clear()
    result = 0
    play_uh(player_coins, pay_cash)


play_uh(player_coins, pay_cash)
