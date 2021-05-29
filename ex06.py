from itertools import count
from itertools import cycle

start_num = int(input('Введите начальное число: '))
stop_num = int(input('Введите последнее число: '))
for i in count(start_num):
    print(i)
    if i >= stop_num:
        break

my_list = [i for i in input('Введите фразу: ').split()]
c = 0
for i in cycle(my_list):
    print(i)
    if c > 10:
        break
    c += 1