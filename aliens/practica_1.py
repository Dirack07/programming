# Taller de web scraping - Code Whit Goz
# Practica 1
# Autor David Beltran
# Descripcion:  Obtener codigo de un documento HTML
#               Utilizaremos la biblioteca urllib
#               https://docs.python.org/3/library/urllib.html

# importaremos la biblioteca urllib

from urllib.request import urlopen

try:
    html = urlopen('https://codewithgoz.com/aliens/')
    print(html.read())
except:
    print('No se puede leer')
else:
    print('Listo!!!')
