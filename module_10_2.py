import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = str(name)
        self.power = int(power)

    def run (self):
        # for i in range(self.power):
        #     print(f'Рыцарь {self.name} в бой с силой {i} ')
        vrag = 100
        day = 0
        print(f'{self.name} на нас напали!!!')
        while vrag:
            vrag -= self.power
            day += 1
            print(f'{self.name} сражается {day} дней, осталось {vrag} воинов.')
            time.sleep(1)
        print(f'{self.name} одержал победу стустя {day} дней.')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')


