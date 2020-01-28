
inputList = str(input('Введите строку: ')).split(' ')
for k in range(0, len(inputList)):
    print(str(k) + ". " + inputList[k][:10])
