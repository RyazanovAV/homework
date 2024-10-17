calls = 0
def count_calls ():
    global calls
    calls = calls + 1
    return calls

def string_info (string):
    count_calls()
    kortez = (len(string), string.upper(), string.lower())
    print(kortez)

def is_contains (string, list_to_search = []):
    count_calls()
    #list_to_search.extend(input('Создаете строку со словами где будут искать =').split())
    for i in (list_to_search):
        if string.lower() == i.lower():
            st = True
            break
        else:
            st = False
    print(st)

string_info(input("Введите текст =>"))
is_contains(input("Введите текст для поиска в строке =>"), input('Создаете строку со словами где будут искать =').split())
string_info(input("Введите текст =>"))
print(calls)
