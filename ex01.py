from sys import argv

file_name, time, sal_hour, bonus = argv
salary = float(time) * float(sal_hour) + float(bonus)
print(f'Зарплата: {salary}')
