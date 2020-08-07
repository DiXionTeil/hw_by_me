import string
import random
import zipfile

# PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):
    """
    Функция открывает архив с паролем и возвращает результат операции (bool)
    """
    try:
        file_to_open.extractall(pwd=password.encode())
        return True
    except Exception as e:
        print(e)
        return False

# len of password is 'n' -> (len_str) symbols
def imaginary_password(len_str):
    res = ''
    for i in range(len_str):
        generate = random.sample(string.digits, 1)
        res += ''.join(generate)
    return res


def hack_archive(file_name, len_of_str):
    """
    Функция брутфорсит запароленный архив
    """
    file_to_open = zipfile.ZipFile(file_name)  # объект архива
    wrong_passwords = []  # список паролей, которые не подошли
    tries = 0  # колличество неудачных попыток

    # processing passwords
    while True:
        password = imaginary_password(len_of_str)
        if password in wrong_passwords:
            continue
        elif extract_archive(file_to_open, password):
            print(f'Archive {file_name} is hacked. Password - {password}')
            print(f'Password was found after {tries} triesn')
            return
        wrong_passwords.append(password)
        tries += 1
        print(tries)
        if tries == 10**len_of_str:
            print('\n─────────────── * WRONG LEN * ───────────────\n')
            wrong_passwords.clear()
            len_of_str += 1
            return hack_archive(file_name, len_of_str)


# ────────── * TESTING * ──────────

filename = 'archive.zip'
hack_archive(filename, 1)

# ─────────────────────────────────