price = 123
bonus = 23
bonus_granted = False 
'''
if bonus_granted:
    price -= bonus

print(price)

'''

dodanyBonus = price -bonus if bonus_granted else price
print(dodanyBonus)

rating = 5
'''
if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('week')
    '''
print('very good' if rating == 5 else 'good' if rating == 4 else 'week' ) 
 
