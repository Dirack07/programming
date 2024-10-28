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
    # Obtener el nombre de las etiquetas html
    print(soup.html.name)
    print('************************************************************************')
    print(soup.head.name)
    print('************************************************************************')
    print(soup.title.name)
    print('************************************************************************')
    print(soup.body.name)
    print('************************************************************************')
    print(soup.p.name)

except:
    print('No se puede leer')
else:
    print('Listo!!!')
