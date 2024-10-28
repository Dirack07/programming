# Taller de web scraping - Code Whit Goz
# Practica 1
# Autor David Beltran
# Descripcion:  Obtener codigo de un documento HTML
#               Utilizaremos la biblioteca urllib
#               https://docs.python.org/3/library/urllib.html

# importaremos las bibliotecas urllib y bs4

from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('https://codewithgoz.com/aliens/')
    soup = BeautifulSoup(html.read(), 'html.parser')
    # Obtener el codigo de las etiquetas html (tare el primer resultado)
    print(soup.html)
    print('************************************************************************')
    print(soup.head)
    print('************************************************************************')
    print(soup.title)
    print('************************************************************************')
    print(soup.body)
    print('************************************************************************')
    print(soup.p)
    print('************************************************************************')
    print(soup.ul)
    print('************************************************************************')
    print(soup.li)
    print('************************************************************************')
    print(soup.a)
    print('************************************************************************')
except:
    print('No se puede leer')
else:
    print('Listo!!!')
