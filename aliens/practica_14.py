# Taller de web scraping - Code Whit Goz
# Practica 13
# Autor David Beltran
# Descripcion:  Obtener todo el texto de un sitio
#               Utilizaremos la biblioteca urllib
#               https://docs.python.org/3/library/urllib.html

# importaremos las bibliotecas urllib y bs4

from urllib.request import urlopen
from bs4 import BeautifulSoup

try:
    html = urlopen('https://codewithgoz.com/aliens/')
    soup = BeautifulSoup(html.read(), 'html.parser')
    # Obtener todo el texto de un sitio
    print('************************************************************************')
    print(soup.get_text())
    print('************************************************************************')

except:
    print('No se puede leer')
else:
    print('Listo!!!')
