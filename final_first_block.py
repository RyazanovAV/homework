grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
gr = [] #Пустой список
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
st = list(students) # Смена типа на список
gr.append(sum(grades[0])/len(grades[0])) #подсчет среденго значения и добавления в пустой список
gr.append(sum(grades[1])/len(grades[1]))
gr.append(sum(grades[2])/len(grades[2]))
gr.append(sum(grades[3])/len(grades[3]))
gr.append(sum(grades[4])/len(grades[4]))
print(gr)
st = list(students)
dict_stud = dict(zip(sorted(st),gr))# Создание словаря с использованием функции zip. Сортировка списка студентов (sorted)
print(dict_stud)

