numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []  # Просты числа
not_primes = []  # Не простые числа

for i in numbers[1:14]:
    is_prime = True
    for j in range(2, i):
        if (i % j) == False:
            not_primes.append(i)
            is_prime = False
            break
    if is_prime != False:
        primes.append(i)
        is_prime = True
print(primes)
print(not_primes)
