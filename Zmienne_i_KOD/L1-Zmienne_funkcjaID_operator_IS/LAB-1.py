a = b = c = 10
print(a, b , c)
print(type(a), type(b), type(c))

print( 'Is value the same?' , a == b == c )
print( 'Are the variables the same?' , a is b is c)
print(id(a), id(b), id(c))

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
b = c = 10
a = 20
print(a, b , c)
print(type(a), type(b), type(c))

print( 'Is value the same?' , a == b == c )
print( 'Are the variables the same?' , a is b is c)
print(id(a), id(b), id(c))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
a = b = c = [1, 2, 3,]
print(a, b, c)
print(type(a), type(b), type(c))
print( 'is value the same?', a == b == c == a)
print( 'are the variables the same', a is b, b is c, c is a)
print(id(a), id(b), id(c))

a = b = c = [1, 2, 3,]
print(a, b, c)
print(id(a), id(b), id(c))

a.append(4)
print(a, b, c)
print(id(a), id(b), id(c))

print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

x =10 
y = 10 
print(id(x), id(y))
y = (y + 1 - 1)
print(id(y))
print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")

y = (y + 1234567890 - 1234567890)
print(id(x), id(y))                          #ID powinny być różne !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                                                                        #a nie SĄ!!!!!!!!!!!!!!!!!!!!!!!!!!!!