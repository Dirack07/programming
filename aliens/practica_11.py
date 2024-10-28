# Taller de web scraping - Code Whit Goz
# Practica 11
# Autor David Beltran
# Descripcion:  Obtener el codigo de una etiqueta de HTML por su ID
#               Utilizaremos la biblioteca urllib
#               https://docs.python.org/3/library/urllib.html

# importaremos las bibliotecas urllib y bs4

from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('https://codewithgoz.com/aliens/')
    soup = BeautifulSoup(html.read(), 'html.parser')
    # Obtener el codigode una etiqueta de HTML por su ID
    print('************************************************************************')
    print(soup.find(id='secret'))
    print('************************************************************************')

except:
    print('No se puede leer')
else:
    print('Listo!!!')
