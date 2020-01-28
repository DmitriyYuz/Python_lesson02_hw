
my_list = ['winter', 'spring', 'summer', 'autumn']
x = int(input('Введите номер месяца от 1 до 12: '))
if x <= 2:
    print(my_list[0])
elif x == 12:
    print(my_list[0])
elif x >= 3 and x <= 5:
    print(my_list[1])
elif x >= 6 and x <= 8:
    print(my_list[2])
elif x >= 9 and x <= 11:
    print(my_list[3])
