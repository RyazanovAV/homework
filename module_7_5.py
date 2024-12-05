from  pprint import pprint
import os
import datetime
import time


print('Тек дир', os.getcwd())

directory = r'D:\phyton_project\myfirstpr\module_7'

for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.abspath(file)
        filetime = os.stat(file).st_mtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        filesize = os.stat(file).st_size
        parent_dir = os.path.abspath(os.path.join(file, os.pardir))
        print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')