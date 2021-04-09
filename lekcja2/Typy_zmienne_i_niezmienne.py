number = 10
print('Variable number:', number, id(number))
number +=2
print('Variable number:', number, id(number))   # to juz nie jest ta sama zmienna 



text =" Africa"
print('Variable text:', text, id(text))
text += "is hot"
print('Variable text:', text, id(text))


print('xooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxooxxoox')

list = [1, 2, 3,]
print('Variable list', list, id(list))
list.append(4)
print('Variable list', list, id(list))
