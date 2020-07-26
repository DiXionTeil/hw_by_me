# 1st task:
from datetime import datetime


def date_converter(input):
    output = datetime.strptime(input, '%b %d %Y %I:%M%p')
    return output


# ────────── * TESTING * ──────────

# input = 'Feb 12 2019 2:41PM'
# print(date_converter(input))

# ─────────────────────────────────


# 2d task:
def is_prime(number):
    if all(number % i != 0 for i in range(2,number)):
        return True
    else:
        return False


# ────────── * TESTING * ──────────

# print(is_prime(2))
# print(is_prime(3))
# print(is_prime(4))
# print(is_prime(5))
# print(is_prime(6))
# print(is_prime(7))
# print(is_prime(8))
# print(is_prime(9))
# print(is_prime(10))
# print(is_prime(11))
# print(is_prime(12))


# ─────────────────────────────────


# 3d task:
def parse(number, input_str):
    result_list = []
    for i in input_str:
        if i in 'idso':
            if i == 'i':
                number += 1
            elif i == 'd':
                number -= 1
            elif i == 's':
                number **= 2
            elif i == 'o':
                result_list.append(number)
    return result_list


# ────────── * TESTING * ──────────

# num = input('Enter your number:\n>')
# while not num.isdigit():
#     is_minus = num.replace('-', '')
#     if not is_minus.isdigit():
#         num = input('NO! Enter 2nd NUMBER as integer, pls:\n>')
#     else:
#         break
# num = int(num)
# string = input('Enter your number:\n>')
# print(parse(num, string))


# ─────────────────────────────────
