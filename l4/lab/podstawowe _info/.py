
print("Kult""\n\"El dupa\"")  #\n -nowa linia \-> powoduje że coś sie pojawia 

#Konkatenacja - łaczeie stringów 
phrase = "Kult & El Dupa"
print(phrase + " to dobry zespół")

print(phrase.lower())
print(phrase.upper())   # małe wielkie litery 

print(phrase.isupper())   # is aprawia ze sprawdza czy litery duze w tym wypadku
print(phrase.upper().isupper())  # tu sprawiamy poprzez upper ze to prawda 


print(len(phrase))      # długośc/  ilosć znaków
 
print(phrase[5:7])      # [ ] ten nawias sprawdza nam pierwsza litere =[0]   poprzez 0:2 pierwsze dwie

print(phrase.index("E"))  # pokazuje nam index na któryej pozycji jest litera u

print(phrase.index("Dup"))  # pokazuje nam index od którego moment zaczyna sie Dup


print(phrase.replace("El", "Ale")) # replace zamienia w tym wypadku frazy 

print(phrase + " to dobre zespoły muzyczne")

print("\./"*31)

# MODULO % reszta z dzielenia
print(10 % 3)

my_num = 7 
print(str(my_num) + " najulubieńsza cyfra to ")   # funkcja str() zmienia podany argument w typ string

my_num = -5 
print(abs(my_num))   #Zwraca wartość bezwzględną liczby -5=5 ale dla liczby dodatniej jest to ta sama liczba dodoatnia 


my_num = 7 
print(pow (3, 2))   #tak jak z potegą 
print(3**2)

print(max(5, 7))  # pokazuje która jest wieksza 
print(min(7, 5))  # pokazuje która jest mniejsza 

print(round(2.9))  # zaokrąglanie 
 

 #      IMPORTOWANIE  
'''from math import * '''   # znaczy że zaimportowane zostaja jakies funkcje w tym wypadku matematyczne 

from math import * 

print(floor(1.2))   # do 1 obniza
print(ceil(1.2))    # do 2 podnosi

print(sqrt(36))     # pierwiastek 

print('-*-'*50)


'''                                                 Wprowadzanie danych '''


''' name = input('Podaj swe imie: ')

print("Helooł " + name + "!!!")

age = input('Podaj swój wiek: ')

print(name + " wygląda na to że w wieku " + age + " jesteś starym dziadem :)")
'''



'''
num1 = input('podaj dowolną liczbę :')

print( "niech będzie to..." + num1 )

num2 = input('podaj kolejną liczbę i je dodaj: ')


'''                                          # mały kalkulator z dodawaniem 
'''
result1 = int(num1) + int(num2)
result2 = input("podaj wynik")



if (int(result2) == int(result1)):
    print(" ok ")
else:
    print(' słabo ')



result = float(num1) + float(num2)
print(result)'''

# 54 minuta 

 # BARDZO CIEKAWE DO OGARNIECIA                     !!!

'''imie = input(" Podaj swoje imię: ")

if imie[-1:] == 'a':                    
    print(" jestes kobietą")
else:
     print('jesteś facetem')'''
     
friends = [ "marcin", "krzysiek", "zbyszek", "gdzie jest zbyszek?", 'zbyszek' ]
print(friends[-1])

print('-*='*50)

lucky_numbers = [5, 7, 13, 21]

#friends.extend(lucky_numbers)
#print(friends)

friends.append( "stachu!")                          #dodajemy staszka :)
print(friends)

#friends.insert(2, "staszek")                        #dodawanie /odejmowanie z listy na któreś miejsce 
#print(friends)

#friends.remove("zbyszek")                           #usuwamy
#print(friends)

#friends.clear()                                        #czyscimyliste
#print(friends)

#friends.pop()                                  #usuwamy ost
#print(friends)
print(friends)
print(friends.index('stachu!'))                     #szukamy stachu!

print(friends.count('zbyszek'))             #liczymi ilość zbyszków

friends.sort()
print(friends)

friends.reverse()
print(friends)


lucky2 = lucky_numbers.copy()                  # kopiowanie odwracanie 
print(lucky2)
lucky2.reverse()
print(lucky2)


print("=+="*41)

coordinates = (5, 7)
#coordinates[1] = 10                               #     TUPLES tak jak listy tylko tam nic nie zmienisz 
print(coordinates[0])

def say_hi(name, age):
    print('witoj juzerze ' + name + " masz " + str(age) + " lat/a ")

say_hi("michal", 31)

def cube(num):
    return num*num*num                                          #RETURN 
result = cube(5)
print



"jestem w restauracji"
'''if ("I WANT MEAT"):
    print("order a steak")
elif ("i want a pasta"):
    print('spagetti')
else:
    print('zamawiam zieleninke')
                                        '''
'''
is_male = False
is_tall = False
if is_male or is_tall:
    print("Uare ara a male, or tall both ")       e 
else:
    print("U are neither male nor tall ")                      
'''# or mozna zamienic na and  i wtedy oba musza być prawdziw
print("____"*21)

is_male = False
is_tall = True


if is_male and is_tall:
    print("U are ara tall male ")       # IF: ELIF: ELSE:                           !!! 
elif is_male and not(is_tall):
    print( " U are short male ")
elif not(is_male) and (is_tall):
    print( " U are not a male bat U are tall ")
else:
    print("U are not a male and U are tall ")      


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2>= num3:
        returnnum2
    else:
        return num3
print(max_num(21, 7, 13))

                                                                #IF else elif
'''
name = input('Podaj swoje imie: ')
print(name)
country = input('Wprowadz nazwe panstwa z ktorego pochodzisz: ')
print(country)
age = (input('Wprowadz swoj wiek: '))


if name[-1:] == 'a':
    print('Jestes kobieta, ktora pochodzi z kraju o nazwie ' + country)
else:
     print('Jestes gościem, ktory pochodzi z ' + country)

if age >= str(18):
    print('i jestes pelnoletni/a')
else:
    print('i nie jestes pelnoletnia')

'''

#KALKULATOR 

print("Wybierz żądaną z dostepnych operacji matematycznych:")
op = input(" + - * /   ")

num1 = input(" Podaj pierwszą liczbę: ")
num2 = input(" Podaj drugą liczbę: ")



if isinstance(num1, (float,int)) == False:
    print('podaj poprawną wartośc  ')
if isinstance(num2, (float,int)) == False:
    print(" podaj poprawną wartość   II")
else:
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "/":
        print(num1 / num2)
    elif op == "*":
        print(num1 * num2)
    else:
        print(" wybierz odpowiednią komendę")



#elif num1 != isinstance(num1, (float,int)) and num2 != isinstance(num2, (float,int)):
#    print("dwa errrrory")


#https://www.youtube.com/watch?v=rfscVS0vtbw&t=12s     #2.04