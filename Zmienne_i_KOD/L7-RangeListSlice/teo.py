'''
for i in range(10):
    print(i)       #wyświetli sie od 0 do 9
print("-"*51)


for i in range(1,11):
    print(i)       #wyświetli sie od 1 do 10
print("-"*51)


for i in range(1,11,2):
    print(i)       #wyświetlą sie tylko nieparzyste 
print("-"*51)

for i in range(10,0,-1):
    print(i)       #wyświetlą się odejmując "-1"  od 10 do 1
print("-"*51)

''' 
for i in range(10,0,-1):
    print(i)

list = list(range(10))
print('List:', list, type(list))

print(list[:-1])       # wyświetla sie od poczatku do przedost..

print(list[:8:2])       # od zerowego do * ale co 2gi z nich 

print('|-|'* 21 )
 
print(list[-1::-1])         #od końca do poczatku cofając się o "1"

print(list[-2:-1]) 


