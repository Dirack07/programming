# Taller de Web Scraping
# Practica 19
# Descripcion: Obtener la informacion de una pagina con BS4

# Importamos las bibliotecas urllib y bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup

# Madar el crawler
html = urlopen('https://codewithgoz.com/gozchenko_maciasnetsov/')
# Cocinamos la sopa
bs = BeautifulSoup(html.read(), 'html.parser')

# Obtenenemos el email, tel. y universidad
contacts = bs.find_all('div', {'class': 'contact'})
contact_list = []
for contact in contacts:
    contact_list.append(contact)
email = contact_list[0].text.replace('\n', '').lstrip()
phone = contact_list[1].text.replace('\n', '').lstrip()
university = contact_list[2].text.replace('\n', '').lstrip()

