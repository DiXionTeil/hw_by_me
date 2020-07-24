# 1st task:
# par 1 ↓
# with open('hw_08_(1)', 'r') as main_file:
#     print(main_file.read())


# par 2 ↓
# with open('hw_08_(1)', 'r') as main_file, open('hw_08_(2)', 'w') as file_to_write:
#     data = main_file.read()
#     file_to_write.write(read)


# par 3 ↓
def read_this(file):
    for i in file.readlines():
        i = str(i)
    file.write('or not read\nso, i don\'t care')
    return file


# with open('hw_08_(1)', 'r') as main_file, open('hw_08_(2)', 'w') as file_to_write:
#     data = main_file.read()
#     file_to_write.write(data)


# with open('hw_08_(2)', 'r+') as file_to_write:
#     read_this(file_to_write)



# 2d task:
# import json

# with open('questions.json', 'r') as json_file:
#     data = json.load(json_file)
#     for q in data['questions']:
#         q['answer'] = input(q['q'] + '\n>')


# with open('questions.json', 'w') as json_file:
#     json.dump(data, json_file, indent = 4)


# 3d task:
import random
input_number = None
shots = 10
first_value_shots = shots
random_num1 = 1
random_num2 = 50


def print_shot_of_shots(shots):
    return f'You have {shots}/{first_value_shots} attempts'


def input_numbers():
    input_number = input('>')
    while not input_number.isdigit():
        input_number = input('Not correct number\nPlease try again!\n>')
    input_number = int(input_number)
    return input_number


def corr_num_range(random_num1, random_num2):
    input_number = input_numbers()
    while not random_num1 - 1 < input_number < random_num2 + 1:
        print(f'Not correct number\nIt must to be from {random_num1} to {random_num2}')
        input_number = input_number()
    return input_number


def game(shots):
    while shots > random_num1 - 1:
        input_number = corr_num_range(random_num1, random_num2)
        if input_number != target_number:
            shots -= 1
            print(print_shot_of_shots(shots))
        elif input_number == target_number:
            print(print_shot_of_shots(shots))
            print('\nYes! You win. My congratulations.')
            global NUMBER1_FOR_STATISTICS, NUMBER2_FOR_STATISTICS
            NUMBER1_FOR_STATISTICS = input_number
            NUMBER2_FOR_STATISTICS = first_value_shots - shots + 1
            return
    else:
        print('\nNo more attempts')
    return


target_number = random.randint(random_num1, random_num2)
print(f'Let\'s play in game with random number\n'
      + print_shot_of_shots(shots)
      + f'\nTry to guess the number from {random_num1} to {random_num2}')
game(shots)

# 4th task:
import json
from datetime import datetime

GOOD_GAME = {
    'The random number': NUMBER1_FOR_STATISTICS,
    'Number of attempt': NUMBER2_FOR_STATISTICS,
    'Date': str(datetime.now())
}

with open('random_number_game.json', 'w') as json_file:
    json.dump(GOOD_GAME, json_file, indent=4)
