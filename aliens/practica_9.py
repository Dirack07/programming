# Taller de web scraping - Code Whit Goz
# Practica 1
# Autor David Beltran
# Descripcion:  Obtener el codigo del papa de la etiqueta html
#               Utilizaremos la biblioteca urllib
#               https://docs.python.org/3/library/urllib.html

# importaremos las bibliotecas urllib y bs4

from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('https://codewithgoz.com/aliens/')
    soup = BeautifulSoup(html.read(), 'html.parser')
    # Obtener el nombre del papa de la eqtiqueta html
    print('************************************************************************')
    print(soup.head.parent)
    print('************************************************************************')
    print(soup.title.parent)
    print('************************************************************************')
    print(soup.body.parent)
    print('************************************************************************')
    print(soup.p.parent)
    print('************************************************************************')

except:
    print('No se puede leer')
else:
    print('Listo!!!')
