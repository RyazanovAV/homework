su = 0
def analiz (data_structure):
    data = (data_structure)
    global su
    lst = []
    for i in data:
        if isinstance(i, (list, tuple, set)):
            lst.extend(analiz(i))
        elif isinstance(i, dict):
            lst.extend(analiz(i.items()))
        else:
            lst.append(i)
            if type(i) == str:
                su = len(i) + su
            else:
                su += i
    return lst

data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])]

resut = analiz(data_structure)
print(resut)
print(su)