#Словари и множества

my_dict = {'Anton': 1985, 'Max': 1990, 'Alex': 1980, 'Pushkin': 1799}
print(my_dict)
print(my_dict['Max'])
print(my_dict.get('Fedor', 'Такого значения не существует'))
my_dict.update({'petr': 1922, 'gleb': 1856})
print(my_dict)
pop_ = my_dict.pop('Pushkin')
print(pop_)
print(my_dict)

my_set = {1, 1, 2, 3, 1, 3, 4, 'List', 'List'}
print(my_set)
my_set.add(9)
my_set.add('hjk')
print(my_set)
my_set.discard(4)
print(my_set)