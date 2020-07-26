import random


# 1st task:
import time

limit_shots = 10
first_value_shots = limit_shots
ras = {'Player 1': '', 'Player 2': ''}

# ────────── * RULES * ────────────

print(f'''
Game:
Two players roll the dices.
The player is win, then who has more victory points from {limit_shots} rolls.

For roll, enter \'\033[1m+\033[0m\'!
For exit - \'\033[1mexit\033[0m\'
Start:''')

# ─────────────────────────────────


# showing steps of game, need to print()
def shots_value(limit_shots):
    percent = limit_shots / first_value_shots
    if percent >= 0.67:
        return f'To \033[1m\033[32m{limit_shots}\033[0m ' \
               f'from \033[1m\033[35m{first_value_shots}\033[0m rolls'  # green / purple
    elif 0.35 < percent < 0.67:
        return f'To \033[1m\033[33m{limit_shots}\033[0m ' \
               f'from \033[1m\033[35m{first_value_shots}\033[0m rolls'  # yellow / purple
    elif percent <= 0.35:
        return f'To \033[1m\033[31m{limit_shots}\033[0m ' \
               f'from \033[1m\033[35m{first_value_shots}\033[0m rolls'  # red / purple


# enter string, need to print()
def roll_input():
    roll_input = input('>')
    while roll_input != '+':
        if roll_input == 'exit':
            exit(0)
        roll_input = input('not correct command:\n>')
    return f'\n'


# basic game count, need to print()
def roll_the_dices(shots):
    count_1p = 0
    count_2p = 0
    while shots >= 1:
        print(roll_input())
        print(shots_value(shots))
        shots -= 1
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        ras['Player 1'] = dice_1
        ras['Player 2'] = dice_2
        if dice_1 == dice_2:
            dice_1 = random.randint(1, 6)
            dice_2 = random.randint(1, 6)
            ras['Player 1'] = dice_1
            ras['Player 2'] = dice_2
        elif dice_1 > dice_2:
            count_1p += 1
        elif dice_1 < dice_2:
            count_2p += 1
        print('Rolling...')
        time.sleep(0.5)
        print(ras)
    else:
        if count_1p > count_2p:
            return f'\nPlayer 1 - \033[1m\033[32mWinner\033[0m!'
        elif count_1p < count_2p:
            return f'\nPlayer 2 - \033[1m\033[32mWinner\033[0m!'
        elif count_1p == count_2p:
            return f'\nNo \033[1m\033[31mWinner\033[0m...'
        exit(0)


# ────────── * TESTING * ──────────

# print(roll_the_dices(limit_shots))

# ─────────────────────────────────


# 2d task:
num_attempts = 2
yes_no = input('Хотите сыграть в \'\033[1m\033[35mУгадайку\033[0m\'?[yes/no]\n>')


def game_yes_no(yes_no):
    while not (yes_no == 'yes' or yes_no == 'no'):
        yes_no = input('...?[yes/no]\n>')
    if yes_no == 'no':
        exit(0)
    elif yes_no == 'yes':
        random_number = random.randint(1, 1000)
        for i in range(num_attempts):
            print(f'У вас {num_attempts - i} попыток!')
            player_select = input('Введите число:\n>')
            while not player_select.isdigit():
                player_select = input('Введите число еще раз:\n>')
            player_select = int(player_select)
            if player_select == random_number:
                print('You win!!!!')
                qwer(yes_no)
            elif player_select > random_number:
                print('Вваше число больше')
            elif player_select < random_number:
                print('Вваше число Меньше')
        else:
            qwer(yes_no)


def qwer(yes_no):
    yes_no_2 = input('\nХотите прожолжить?[yes/no]\n>')
    while not (yes_no_2 == 'yes' or yes_no_2 == 'no'):
        yes_no_2 = input('...?[yes/no]\n>')
    else:
        if yes_no_2 == 'no':
            exit(0)
        elif yes_no_2 == 'yes':
            print(game_yes_no(yes_no))


# ────────── * TESTING * ──────────

# game_yes_no(yes_no)

# ─────────────────────────────────