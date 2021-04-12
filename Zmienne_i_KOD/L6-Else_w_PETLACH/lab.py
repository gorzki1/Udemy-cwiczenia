
print('-----------------------MOJE---------------------------------------')
import urllib.request
import os

data_dir = 'C:/Users/user/Desktop/Udemy Cwiczenia/l4'

pages = [

    { 'name': 'Zgierz',      'url': 'https://zgierz.praca.gov.pl/'}, 

    { 'name': 'WikiImiona', 'url': 'https://pl.wikipedia.org/wiki/Najpopularniejsze_imiona' },

    { 'name': 'KFC',       'url': 'https://kfc.pl/main/home/menu'} ]

for page in pages:

    try: 
        file_name = "{}.html".format(page['name'])
        path = os.path.join(data_dir, file_name)

        print("Processing: {} => {} ...".format(page["url"], file_name))
        urllib.request.urlretrieve (page["url"], path)
        print('...done')

    except:
       print('FAILURE processing web page: {}'.format(page['name']))
       print('Stopping the process!')
       break
else:
    print('all pages downloaded succesfully')