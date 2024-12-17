import threading
import time

def wite_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i} \n')
            time.sleep(0.1)
            # print(i, threading.current_thread())
            # print(threading.enumerate())
        print(f'Завершилась запись в файл {file_name}')

start = time.time()
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(45, 'example3.txt')
wite_words(30, 'example4.txt')
stop = time.time()
print(time.strftime("%H:%M:%S", time.gmtime(stop - start)))

start = time.time()
t1 = threading.Thread(target=wite_words, args=(10, 'example5.txt'))
t2 = threading.Thread(target=wite_words, args=(30, 'example6.txt'))
t3 = threading.Thread(target=wite_words, args=(45, 'example7.txt'))
t4 = threading.Thread(target=wite_words, args=(35, 'example8.txt'))
t1.start()
t2.start()
t3.start()
t4.start()
t1.join()
t2.join()
t3.join()
t4.join()
stop = time.time()
print(time.strftime("%H:%M:%S", time.gmtime(stop - start)))
