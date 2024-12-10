class Car:
    def __init__(self, model, __vin, __numbers):
        self.model = model
        self.__vin = __vin
        self.__numbers = __numbers
        self.__is_valid_vin(__vin)
        self.__is_valid_numbers(__numbers)

    def __is_valid_vin(self, vin_number):
        if isinstance(vin_number, int) != True:
            raise IncorrectVinNumber('Некорректный тип vin номер')
        elif vin_number > 9999999 or vin_number < 1000000:
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        else:
            return True

    def __is_valid_numbers(self, numbers):
        if isinstance(numbers, str) != True:
            raise IncorrectCarNumbers('Некорректный тип vin номер')
        elif len(numbers) != 6:
            raise IncorrectCarNumbers('Неверный тип для vin номера')
        else:
            return True

class IncorrectVinNumber(Exception):
    def __init__(self, message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')
try:
   second = Car('Model2', 30000, 'т001тр')
except IncorrectVinNumber as exc:
   print(exc.message)
except IncorrectCarNumbers as exc:
   print(exc.message)
else:
   print(f'{second.model} успешно создан')
try:
   third = Car('Model3', 4000000, 'нет номера')
except IncorrectVinNumber as exc:
   print(exc.message)
except IncorrectCarNumbers as exc:
   print(exc.message)
else:
   print(f'{third.model} успешно создан')


