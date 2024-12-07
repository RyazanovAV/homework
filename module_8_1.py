def add_everything_up(a, b):
    try:
        return a + b
    except TypeError:
        s_tr = (f'{a} {b}')
        return s_tr

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))