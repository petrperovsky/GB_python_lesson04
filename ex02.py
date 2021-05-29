from random import randint

my_list = [randint(0, 100) for i in range(15)]
new_list = [el for n, el in enumerate(my_list) if my_list[n - 1] < my_list[n]]

print(my_list)
print(new_list)