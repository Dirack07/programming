# Taller de Web Scraping - Code With Goz
# Zelda Web Scrapper
# Descripción: Ejercicio extra

# Importamos las bibliotecas utllib y bs4
import requests
import urllib.request
from bs4 import BeautifulSoup
import time

main_url = 'https://vandal.elespanol.com/guias/guia-the-legend-of-zelda-tears-of-the-kingdom-trucos-consejos-y-secretos/armaduras-normales#armadura-arcaica'
headers = {
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}


def get_all_info_from_page(url):
    # Mandar al crawler
    html = requests.get(url, headers=headers)
    # Cocinamos la sopa
    soup = BeautifulSoup(html.content, 'html.parser')
    # Obtenemos las imágenes
    images = soup.find_all('img')

    good_images = []

    for image in images:
        try:
            image_description = []
            image_description.append(image.get('data-src'))
            image_description.append(image.get('alt'))
            good_images.append(image_description)
        except:
            print("No tiene data-src")

    for image in good_images:
        try:
            title = image[1].replace(' ', '_')
            title = title.replace(
                'The_Legend_of_Zelda:_Tears_of_the_Kingdom_-_', '')
            title = title.replace(
                'The_legend_of_Zelda:_Tears_of_the_Kingdom_-_', '')
            title = title.replace(
                'The_Legend_of_Zelda_Tears_of_the_Kingdom_-_', '')

            # Descargamos la imagen
            urllib.request.urlretrieve(
                image[0], f"/home/goz/Cursos/python_web_scraping/extra/{title}.jpg")
            print('Imagen descargada')
        except:
            print("No se puede descargar")
        time.sleep(3)


get_all_info_from_page(main_url)
