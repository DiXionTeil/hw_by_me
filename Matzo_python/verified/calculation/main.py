import add, divide, multiply, subtraction

if __name__ == '__main__':
    print("""
    ╔═══════════════════════════════════════════════════╗
    ║                                                   ║
    ║   The calculator provides you next functions:     ║
    ║   If you want add, click "+";                     ║
    ║   If you want subtraction, click "-";             ║
    ║   If you want multiply, click "*";                ║
    ║   If you want divide, click "/";                  ║
    ║   If you want integer division, click "//";       ║
    ║   If you want to exit the program, enter "exit";  ║
    ║                                                   ║
    ╚═══════════════════════════════════════════════════╝
    """)
    command = 1
    while command != 0:

        # first number
        first_operand = input('Enter 1st number, pls:\n>')
        while not first_operand.isdigit():
            if first_operand == 'exit':
                print('So, you want to loose. ok...')
                exit(0)
            else:
                is_minus = first_operand.replace('-', '')
                if not is_minus.isdigit():
                    print(first_operand)
                    first_operand = input('NO! Enter 1st NUMBER as integer, pls:\n>')
                else:
                    break
        first_operand = int(first_operand)
        print(first_operand)

        # function
        function_in = input('Enter that function, what the prog. offer (look up):\n>')
        while not function_in.isdigit():
            if function_in == 'exit':
                print('So, you want to loose. ok...')
                exit(0)
            elif function_in == '+':
                break
            elif function_in == '-':
                break
            elif function_in == '*':
                break
            elif function_in == '/':
                break
            elif function_in == '//':
                break
            else:
                function_in = input("I don't know this function. Try again, pls:\n>")

        # second number
        second_operand = input('Enter 2nd number, pls:\n>')
        while not second_operand.isdigit():
            if second_operand == 'exit':
                print('So, you want to loose. ok...')
                exit(0)
            else:
                is_minus = second_operand.replace('-', '')
                if not is_minus.isdigit():
                    print(second_operand)
                    second_operand = input('NO! Enter 2nd NUMBER as integer, pls:\n>')
                else:
                    break
        second_operand = int(second_operand)

        # equals
        if function_in == '+':
            equals = add.add(first_operand, second_operand)
        elif function_in == '-':
            equals = subtraction.subtraction(first_operand, second_operand)
        elif function_in == '*':
            equals = multiply.multiply(first_operand, second_operand)
        elif function_in == '/':
            equals = divide.divide(first_operand, second_operand)
        elif function_in == '//':
            equals = divide.int_divide(first_operand, second_operand)

        # result
        print(f'{first_operand} {function_in} {second_operand} =', equals)
    else:
        exit(0)
