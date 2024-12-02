from  pprint import pprint
import os
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]
def custom_write(file_name, strings):

    info_1 = {}
    file_1 = open(file_name, 'w', encoding='utf-8')
    for a in strings:
        file_1.write(a + "\n")
    file_1.close()
    file_1 = open(file_name, 'r' , encoding='utf-8')
    f = len(file_1.readlines())
    file_1.seek(0)
    for b in range(1, f+1):
        tl = file_1.tell()
        op = file_1.readline()
        info_1[b, tl] = op
    return info_1

result = custom_write('test.txt', info)

for elem in result.items():

  print(elem)

