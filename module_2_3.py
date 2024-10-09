my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
print(my_list)

index_list = 0  # Первый вариант, выводим положительные числа игнорируя "0" до первого отрицательного
while index_list < len(my_list):
    if my_list[index_list] == 0:
        index_list = index_list + 1
    elif my_list[index_list] > 0:
        print(my_list[index_list])
        index_list = index_list + 1
    else:
        break

print('')

index_list = 0  # Второй вариант, если отрицательно - то выход из цикла, если "0" то индекс + 1, остальные выводим и +1
while index_list < len(my_list):
    if my_list[index_list] < 0:
        break
    elif my_list[index_list] == 0:
        index_list = index_list + 1
        continue
    print(my_list[index_list])
    index_list = index_list + 1


