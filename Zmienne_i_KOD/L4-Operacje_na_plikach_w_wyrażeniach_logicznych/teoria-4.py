import os

path = r'C:\Users\user\Desktop\udemy cwiczenia/l4>'

os.remove(path)

if os.path.isfile(path):
    print('file exists' % path)
else:
    print('Creating a file %s' % path)
    open(path, 'x').close()
    print('File %s created' % path)

