from random import randint

my_list = [randint(0, 100) for i in range(15)]
new_list = [i for i in my_list if my_list.count(i) == 1]

print(new_list)