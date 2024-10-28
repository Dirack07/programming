# Taller de web Scraping - Code With Goz
# Práctica 3
# Autor: Goz
# Descripción: Obtener código de un documento HTML y presentarlo
#              en un formato fácil de leer
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizarmoes la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen(
        'https://codewithgoz.com/gozchenko_maciasnetsov/index2.html')
    soup = BeautifulSoup(html.read(), 'html.parser')
    print(soup.prettify())
except:
    print('No se pudo abrir')
else:
    print('Listo!!!')
