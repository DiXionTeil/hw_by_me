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
import json

# with open('questions.json', 'r') as json_file:
#     data = json.load(json_file)
#     for q in data['questions']:
#         q['answer'] = input(q['q'] + '\n>')


# with open('questions.json', 'w') as json_file:
#     json.dump(data, json_file, indent = 4)


# 3d task:
import random
INPUT_NUMBER = None
SHOTS = 10
FIRST_VALUE_SHOTS = SHOTS
RANDOM_NUM1 = 1
RANDOM_NUM2 = 50


def print_shot_of_shots(SHOTS):
    return f'You have {SHOTS}/{FIRST_VALUE_SHOTS} attempts'


target_number = random.randint(RANDOM_NUM1, RANDOM_NUM2)
print(target_number)
print(f'Let\'s play in game with random number\n'
      + print_shot_of_shots(SHOTS)
      + f'\nTry to guess the number from {RANDOM_NUM1} to {RANDOM_NUM2}')


def input_number():
    INPUT_NUMBER = input('>')
    while not INPUT_NUMBER.isdigit():
        INPUT_NUMBER = input('Not correct number\nPlease try again!\n>')
    else:
        INPUT_NUMBER = int(INPUT_NUMBER)
    return INPUT_NUMBER


def corr_num_range(RANDOM_NUM1, RANDOM_NUM2):
    while not RANDOM_NUM1 - 1 < input_number() < RANDOM_NUM2 + 1:
        print(f'Not correct number\nIt must to be from {RANDOM_NUM1} to {RANDOM_NUM2}')
    return INPUT_NUMBER


while SHOTS > RANDOM_NUM1 - 1:
    corr_num_range(RANDOM_NUM1, RANDOM_NUM2)
    if INPUT_NUMBER != target_number:
        SHOTS -= 1
        print(print_shot_of_shots(SHOTS))
    elif INPUT_NUMBER == target_number:
        print(print_shot_of_shots(SHOTS))
        print('\nYes! You win. My congratulations.')
        exit(0)
else:
    print('\nNo more attempts')
    exit(0)







#
# while SHOTS > 0:
#     if corr_num_range(INPUT_NUMBER, RANDOM_NUM1, RANDOM_NUM2) != target_number:
#         SHOTS -= 1
#         print(print_shot_of_shots() + 'Try again:\n')
#         input_number()
#     else:
#         SHOTS = 0
#         print('No more attempts')
#         exit(0)



# while RANDOM_NUM1 - 1 < input_num < RANDOM_NUM2 + 1:
#     while SHOTS > 0:
#         if input_num != target_number:
#             SHOTS -= 1
#             print(print_shot_of_shots)
#         else:
#             print('Yes! You win. My congratulations.')
#     else:
#         print('No more attempts')
#         exit(0)
# else:
#     input_num = input(f'Not correct number\nIt must to be from {RANDOM_NUM1} to {RANDOM_NUM2}\n>')

