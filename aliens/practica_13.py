# Taller de web scraping - Code Whit Goz
# Practica 13
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
    # Obtener todas las imagenes de un sitio
    print('************************************************************************')
    for link in soup.find_all('img'):
        print(link.get('src'))
    print('************************************************************************')

except:
    print('No se puede leer')
else:
    print('Listo!!!')
