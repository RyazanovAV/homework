def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
values_list = [555, 'fd' , False]
values_dict = {'a': 1, 'b': 'sdfs', 'c':False}
#print_params()

print_params(b = 25)
print_params(c = [1,2,3])
print_params(*values_list)
print_params(values_list, 'bdd')

print_params(**values_dict)
print_params(values_dict, 787)

values_list_2 = ['qqqqq', 332]
print_params(*values_list_2, 42)  #Работает !!!
