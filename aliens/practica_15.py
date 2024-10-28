# Taller de web Scraping - Code With Goz
# Práctica 15
# Autor: Goz
# Descripción: Obtener toda la información de un sitio web
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizarmoes la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

try:
    # Nuestro crawler va a la url
    html = urlopen('https://codewithgoz.com/aliens/')
    # Se prepara la sopa
    soup = BeautifulSoup(html.read(), 'html.parser')
    # Creamos una lista para todos los links
    links = []
    # Obtener todoas los enlaces del sitio
    for link in soup.find_all('a'):
        links.append(link.get('href'))
except:
    print('No se pudo abrir')
else:
    print('Listo!!!')


# Creamos un diccionario para todos los aliens
aliens = {}


for link in links:
    try:
        # Nuestro crawler va a la url
        html = urlopen('https://codewithgoz.com/aliens/' + link)
        # Se prepara la sopa
        soup = BeautifulSoup(html.read(), 'html.parser')
        # Obtener el nombre del alien
        name = soup.h1.string
        # Obtener la descipción del alien
        content = soup.find(id='content').p.string.replace(
            '\n', '').rstrip().lstrip()
        # Agregamos la información al diccionario
        aliens[name] = re.sub(' +', ' ', content)
    except:
        print('No se pudo abrir')
    else:
        print('Listo!!!')

print(aliens)
