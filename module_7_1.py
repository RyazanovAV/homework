from  pprint import pprint
import os
class Product:
    def __init__ (self, name, weight, category):
        self.name = str(name)
        self.weight = float(weight)
        self.category = str(category)

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')

    # def __repr__(self):
    #     return self.name, self.weight, self.category
class Shop:
    __file_name = 'products.txt'
    def __init__(self):
        if not os.path.isfile(self.__file_name):
            file = open(self.__file_name, 'w')
            file.close()

    def get_products(self):
        a = ''
        file = open(self.__file_name, 'r')
        a = file.read()
        print(a)
        file.close()
    def add(self, *products):
        file = open(self.__file_name, 'r')
        lines = ()
        lines = file.readlines()
        file.close()
        if len(lines) == 0:
            file = open(self.__file_name, 'w')
            for b in products:
                file.write(str(b) + "\n")
            file.close()
        else:
            for l2 in products:
                for l1 in lines:
                    if l2.name in l1:
                        m = True
                        break
                    else:
                        m = False
                if m == True:
                    print('Продукт ', l2, 'уже есть в магазине')
                else:
                    file = open(self.__file_name, 'a')
                    file.write(str(l2) + "\n")
                    file.close()

s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1,p2,p3)
print(s1.get_products())