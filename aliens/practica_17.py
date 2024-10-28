# Taller de Web Scraping - Code With Goz
# Práctica 17
# Autor: Goz
# Descripción: Obtener toda la información del sitio web
#              Utilizaremos la biblioteca urllib
#              https://docs.python.org/3/library/urllib.html
#              Utilizaremos la biblioteca bs4
#              https://www.crummy.com/software/BeautifulSoup/bs4/doc/


# Importamos las bibliotecas urllib y bs4
import urllib3
import urllib.request
from bs4 import BeautifulSoup
import re
import time
import csv

target_website = 'https://codewithgoz.com/aliens/'

# Creamos una instancia del poolmanager
http = urllib3.PoolManager()

# Definimos la información del header
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}

try:
    # Nuestro crawler va a la url
    html = http.request('GET', target_website, headers=headers)
    # Se prepara la sopa
    soup = BeautifulSoup(html.data.decode('utf-8'), 'html.parser')
    # Creamos una lista para todos los links
    links = []
    # Obtener todos los enlaces de un sitio
    for link in soup.find_all('a'):
        links.append(link.get('href'))
except:
    print("No se puede abrir")

# Creamos un diccionario para todos los aliens
aliens = {}

for link in links:
    try:
        time.sleep(3)
        print('Ingresamos a https://codewithgoz.com/aliens/' + link)
        # Nuestro crawler va a la url
        html = http.request('GET', target_website + link, headers=headers)
        # Se prepara la sopa
        soup = BeautifulSoup(html.data.decode('utf-8'), 'html.parser')
        # Obtenemos el nombre del alien
        name = soup.h1.string
        # Obtenemos la descripción del alien
        content = soup.find(id='content').p.string.replace(
            '\n', '').rstrip().lstrip()
        # Agregamos la información al diccionario
        aliens[name] = re.sub(' +', ' ', content)
        # Obtenemos la imagen del alien
        image = soup.img.get('src')
        image_url = "https://codewithgoz.com/aliens/" + image
        image_file = image.replace("images/", "")
        urllib.request.urlretrieve(
            image_url, f"/home/goz/Cursos/python_web_scraping/clase2/{image_file}")
        print('Información recopilada!!!')
    except:
        print("Hubo un error")


# Agregamos información a un csv
with open('/home/goz/Cursos/python_web_scraping/clase2/aliens.csv', 'a', newline='', encoding='utf-8') as f:
    file = csv.writer(f)
    for key, value in aliens.items():
        file.writerow([key, value])
