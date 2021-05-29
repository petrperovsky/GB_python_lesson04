from math import factorial

n = int(input('Введите число: '))
def my_fact():
    global n
    for i in range(1, n + 1):
        yield factorial(i)

gen = my_fact()

for i, el in enumerate(gen, 1):
    print(f'{i}! = {el}')