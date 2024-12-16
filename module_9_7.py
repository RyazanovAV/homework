
def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        r = result
        for i in range(2, int(r ** 0.5) + 1):
            if r % i == 0:
                print("Число не простое")
                return result
        print("Число простое")
        return result
    return wrapper
@is_prime
def sum_three(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

print(sum_three(2, 3, 6))


