''''''
'''
─────── <  1  > ───────
построить функцию, кот возвращает массив в виде строки (str):
от N_min до N_max, например:
от 0 до n ↓

    0  1  2 ...  n
    1  2 ... n + 1
    2 ...... n + 2
    ..............
    n+1  n+2 ... N

'''
def massive_min_max(min_val: int, n: int):
    def massive_n(n, min_val):
        mass_n = f'{min_val}'
        for i in range(min_val + 1, n + 1):
            mass_n += '\t' + ''.join(str(i))
        return mass_n

    mass = ''
    for i in range(min_val, n + 1):
        mass += massive_n(n, min_val) + '\n'
        n += 1
        min_val += 1
    return mass


# ────────── * TESTING * ──────────

# print(massive_min_max(0, 4))
# print(massive_min_max(-5, 5))

# ─────────────────────────────────
'''
─────── <  2  > ───────
построить функцию, кот возвращает массив в виде строки (str):
от |N_min| до N_max, например:
от |-2| до n ↓

    2  1  0  1 ...  n
    1  0  1 ... n + 1
    0  1  2 ... n + 2
    .................
    n  n+1 n+2 .... N

'''
def massive_cro_min_max(min_val: int, n: int):
    def massive_n(n, min_val):
        mass_n = f'{abs(min_val)}'
        for i in range(min_val + 1, n + 1):
            mass_n += '\t' + ''.join(str(abs(i)))
        return mass_n

    mass = ''
    for i in range(min_val, n + 1):
        mass += massive_n(n, min_val) + '\n'
        n += 1
        min_val += 1
    return mass


# ────────── * TESTING * ──────────

print(massive_cro_min_max(0, 4))
print(massive_cro_min_max(-2, 5))

# ─────────────────────────────────
'''
─────── <  3  > ───────
построить функцию, кот возвращает массив в виде строки (str):
от |N_min| до N_max, например:
от |-1| до n ↓

    1  0  1  2 ...  n
    0  1  2 ... n - 1
    1  0  1 ... n - 2
    .................
    n  n-1 n-2 .... 1

'''