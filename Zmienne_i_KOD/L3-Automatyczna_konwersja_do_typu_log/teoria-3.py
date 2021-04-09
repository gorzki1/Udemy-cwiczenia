isOk = 'True'
print(" Variable isOk: ", isOk, type(isOk))
if isOk:
    print('TRUE')

    isOk = 'ISOK'
print(" Variable isOk: ", isOk, type(isOk))
if isOk:
    print('TRUE')


    isOk = 'PYTHON'
print(" Variable isOk: ", isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = ''
print(" Variable isOk: ", isOk, type(isOk))
if isOk:
    print('TRUE')                                  # JESLI W ZMIENNEJ NAPIS JEST NIEPUSTY TO ZAWSZE WYJDZIE PRAWDA!
                                                        #NAPIS PUSTY INTERPRETUJE JAKOW fałsz


isOk = 1
print(" Variable isOk: ", isOk, type(isOk))
if isOk:
    print('TRUE')


isOk = 0
print(" Variable isOk: ", isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = [1,2,3]
print(" Variable isOk: ", isOk, type(isOk))
if isOk:
    print('TRUE')                               #jak będą same 0 to nadal bedzie prawda TRUE

isOk = []
print(" Variable isOk: ", isOk, type(isOk))
if isOk:
    print('TRUE')

isOk = [0,0,0,0]
print(" Variable isOk: ", isOk, type(isOk))
if isOk[0]:
    print('TRUE')                                  #zerowym elementem jest 0 a zero konwertuje się 0  więc FAŁSZ


listOfErrors = [100,101,102]
print('Variable isOK', listOfErrors, type(listOfErrors))
if len(listOfErrors) > 0:
    print('ERROR')