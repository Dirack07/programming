# Taller de web scraping - Code Whit Goz
# Practica 10
# Autor David Beltran
# Descripcion:  Obtener el nombre nombre de la clase de la etiqueta
#               Utilizaremos la biblioteca urllib
#               https://docs.python.org/3/library/urllib.html

# importaremos las bibliotecas urllib y bs4

from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('https://codewithgoz.com/aliens/')
    soup = BeautifulSoup(html.read(), 'html.parser')
    # Obtener el nombre de la clase de la clase de la eqtiqueta
    print('************************************************************************')
    print(soup.p['class'])
    print('************************************************************************')

except:
    print('No se puede leer')
else:
    print('Listo!!!')
