
my_list = [7, 5, 3, 3, 2]
print(my_list)
k = int(input("Новый элемент: "))
for i in range(len(my_list)):
    if my_list[i] == k:
        my_list.insert(i + 1, k)
        break
    elif my_list[0] < k:
        my_list.insert(0, k)
        break
    elif my_list[-1] > k:
        my_list.append(k)
        break
    elif my_list[i] > k and my_list[i + 1] < k:
        my_list.insert(i + 1, k)
        break
print(my_list)
