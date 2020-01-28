
my_list = []
e = 0
r = int(input('Сколько вы внесете елементов? '))
while e < r:
    x = input('Текущий элемент: ')
    my_list.append(x)
    e = e + 1
y = 0
while y < r-1:
    temp = my_list[y]
    my_list[y] = my_list[y+1]
    my_list[y+1] = temp
    y = y + 2
print(my_list)
