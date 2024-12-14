from pprint import pprint
import random

class MysticBall:
    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)

first = 'Мама мыла раму'
second = 'Рамена мало было'
print(list(map(lambda x, y: x == y , first, second)))

def get_advanced_writer(file_name):
    def write_everything(*data_set):
        file_1 = open(file_name, 'w')
        file_1.write(str(data_set))
        file_1.close()
    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 'в', 'списке'])

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())


