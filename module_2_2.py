one = int(input ('Введите первое число: '))
two = int(input ('Введите второе число: '))
three = int(input ('Введите третье число: '))

#if one == two and two == three and one == three:  # Первый вариант
if (one+two+three)/one == 3:                       # Второй вариант
    print ('3')
elif one == two or two == three or one == three:
    print('2')
else:
    print ('0')