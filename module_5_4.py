class House:
    houses_history = []
    def __new__(cls, *args, **kwargs):
        #House.houses_history.append(args[0]) #Обращение через класс. Тоже работает
        cls.houses_history.append(args[0])
        return super().__new__(cls)

    def  __init__(self, name, floor):
        self.name = str(name)
        self.number_of_floors = floor
        # House.houses_history.append(name) #Тестовый вариант

    def __del__(self):
        print(f'{self.name}снесён, но он останется в истории')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return(f'{self.name}, кол-во этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        self.new_floor =  new_floor
        if self.new_floor >= 1 and self.new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i+1)
        else:
            print('Такого этажа не существует')

#__eq__(==), __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=)
    def __eq__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'Неверный тип {other}')
        else:
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'Неверный тип {other}')
        else:
            return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'Неверный тип {other}')
        else:
            return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'Неверный тип {other}')
        else:
            return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'Неверный тип {other}')
        else:
            return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        if not isinstance(other.number_of_floors, int):
            print(f'Неверный тип {other}')
        else:
            return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            print(f'Неверный тип {value}')
        else:
            self.number_of_floors = self.number_of_floors + value
            return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

# h1 = House('ЖК Горский', 10)
# h2 = House('Домик в деревне', 20)
#
# print(h1)
# print(h2)
# print(h1 == h2) # __eq__
# h1 = h1 + 10 # __add__
# print(h1)
# print(h1 == h2)
# h1 += 10 # __iadd__
# print(h1)
# h2 = 10 + h2 # __radd__
# print(h2)
# print(h1 > h2) # __gt__
# print(h1 >= h2) # __ge__
# print(h1 < h2) # __lt__
# print(h1 <= h2) # __le__
# print(h1 != h2) # __ne__
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

del h2
del h3
print(House.houses_history)