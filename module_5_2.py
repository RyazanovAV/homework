class House:
    def  __init__(self, name, floor):
        self.name = str(name)
        self.number_of_floors = int(floor)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return(f'{self.name}, кол-во этажей: {self.number_of_floors}')

    def go_to(self, new_floor):
        self.new_floor =  int(new_floor)
        if self.new_floor >= 1 and self.new_floor <= self.number_of_floors:
            for i in range(new_floor):
                print(i+1)
        else:
            print('Такого этажа не существует')

h1 = House('ЖК Горский', 10)
h2 = House('Домик в деревне', 20)
# h1.go_to(5)
# h2.go_to(3)

# # __str__
print(h1)
print(h2)
# # __len__
print(len(h1))
print(len(h2))