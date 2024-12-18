import random
import threading
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def deposit(self):
        for opq in range(1, 101):
            ra = random.randint(50, 500)
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            elif self.balance >= 500:
                pass
            else:
                self.balance += ra
                print(f'Пополнение: {ra}. Баланс: {self.balance}')
                time.sleep(0.01)

    def take(self):
        for op in range(1, 101):
            ra = random.randint(50, 500)
            print(f'Запрос на случайное число: {ra}')
            time.sleep(0.01)
            if ra < self.balance:
                self.balance -= ra
                print(f'Снятие: {ra}. Баланс: {self.balance}')
                time.sleep(0.01)
            else:
                print(f'Запрос отклонён, недостаточно средст')
                self.lock.acquire(timeout= 1)
                time.sleep(0.01)



bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')



