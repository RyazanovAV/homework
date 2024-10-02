#Неизменяемые и изменяемые объекты. Кортежи

immutable_var = 1, 2, "text", True
print (immutable_var)
immutable_var_1 = tuple([1, 2, "text", False])
print (immutable_var_1)
print (immutable_var[1])
print (immutable_var_1[3])
#immutable_var[1] = 3 # Ошибка элемент типа кортеж(tuple) изменить нельзя
immutable_list = [2, 1, 'text_2', False]
print(immutable_list)
immutable_list[2] = 'hello'
#immutable_list = 3, 4
print(immutable_list)
print(immutable_list[1::-1])
