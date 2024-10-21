calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    count_calls()
    kortez = (len(string), string.upper(), string.lower())
    return kortez


def is_contains(string, list_to_search=None):
    count_calls()
    #list_to_search.extend(input('Создаете строку со словами где будут искать =').split())
    for i in (list_to_search):
        if string.lower() == i.lower():
            st = True
            break
        else:
            st = False
    return st

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
