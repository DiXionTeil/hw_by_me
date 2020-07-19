def divide(a, b):
    try:
        c = a / b
    except ZeroDivisionError:
        c = print('Not divide by zero')
    return c


def int_divide(a, b):
    try:
        c = a // b
    except ZeroDivisionError:
        c = print('Not divide by zero')
    return c