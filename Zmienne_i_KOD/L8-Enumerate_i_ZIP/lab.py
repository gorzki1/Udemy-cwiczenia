

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']

projectsLeaders = list(zip(projects,leaders))
#print(projectsLeaders)

for p, l in projectsLeaders:
    print('The leader of', p, 'is', l) 






     # na chłopski rozum to było 

projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
dates = ['2016-06-23', '2016-08-29', '1994-01-01']

#position = [1, 2, 3]

projectsLeaders = list(zip(projects,dates,leaders))
print(projectsLeaders)
for p, d, l in projectsLeaders:
    print('The leader of "{}" started {} is {}'.format(p,d,l)) 

print('^'*51)
for pos, (p, d, l) in enumerate(zip(projects,dates,leaders)):
    print( pos+1, 'The leader of', p, 'started', d, 'is', l)












  
'''
   projects = ['Brexit', 'Nord Stream', 'US Mexico Border']
leaders = ['Theresa May', 'Wladimir Putin', 'Donald Trump and Bill Clinton']
 
for p, l in zip(projects, leaders):
    print('The leader of "{}" is {}'.format(p,l))
 
 
dates = ['2016-06-23', '2016-08-29', '1994-01-01']
 
for p, l,d in zip(projects, leaders, dates):
    print('The leader of "{}" started {} is {}'.format(p,d,l))
 
 
for i, (p,l,d) in enumerate(zip(projects, leaders, dates)):
    print('{} - The leader of "{}" started {} is {}'.format(i+1,p,d,l))
 '''

 # tak powinno być 