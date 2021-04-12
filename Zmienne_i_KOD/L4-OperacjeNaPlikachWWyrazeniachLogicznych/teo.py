import os

path = r'C:\Users\user\Desktop\Udemy Cwiczenia\l4\readme.txt'



 #os.remove(path)
'''
if os.path.isfile(path):
    print('file exists' % path)
else:
    print('Creating a file %s' % path)
    open(path, 'x').close()
    print('File %s created' % path)

'''



result = os.path.isfile(path) or open(path, 'x').close()
print(result)

