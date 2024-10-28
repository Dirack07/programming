# Cadenas de texto en python (Strings)

name_1 = "Martha"
print(name_1)
print(type(name_1))
print(id(name_1))

name_1 = "Susana"
print(name_1)
print(type(name_1))
print(id(name_1))

phrase = "Homer's baseball bata is in the house"
print(phrase)

phrase = '"El Barto" is here'
print(phrase)

alien_song = '''
Los marcianos llegaron ya
y llegaron bailando
cha cha cha
'''
print(alien_song)

# Caracteres de escape
song = "Los marcianos llegaron ya \n y llegaron bailando \n cha cha cha"
print(song)

song = "Los marcianos llegaron ya \t y llegaron bailando \t cha cha cha"
print(song)

my_text = "\"Mexico\" es el mejor pais de todos porque hay tacos"
print(my_text)

my_text = 'Carmelo\'s dog is crazy'
print(my_text)

my_text = 'Quiero una diagonal invertida \\'
print(my_text)

my_text = "Mexico es el mejor pais de todos \f porque hay tacos"
print(my_text)

my_text = "Mexico es el mejor pais de todos \v porque hay tacos"
print(my_text)

bytes_content = b'\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(type(bytes_content))
print(bytes_content.decode('utf-16'))

bytes_content2 = '\xcf\x84o\xcf\x81\xce\xbdo\xcf\x82'
print(type(bytes_content2))

# Bytes literales
# Exadecimal
print('\x40')
# Octal
print('\100')

# Unicode literales
print('\N{GREEK CAPITAL LETTER DELTA}')  # Unicode database id
print('\u0394')  # Unicode char 16 bit hex val
print('\U00000394')  # Unicode char 32 bit hex val
print('\N{Grinning Face with Smiling Eyes}')
print('\U0001F601')  # Unicode char 32 bit hex val
print("Hola yo soy una \"estuoenda\" \n \U0001F412 cadena ")

# Cadenas raw
csv1 = R"C:\Documentos\new\programas\text1.csv"
print(csv1)

print(len('heroe'))

# Concatenar cadenas
word_1 = 'bat'
word_2 = 'man'
heroe = word_1 + word_2
print(heroe)

# Repetir cadenas
word = 'na'
print(word*80)

# Indexado de cadenas
word_3 = 'GOMG8219177P8'
print(word_3[4] + word_3[5])
print(word_3[-1])

# Slicing de cadenas
word_4 = 'Wayne is Batman'
print(word_4[0:8])
print(word_4[1:8])
print(word_4[4:])
print(word_4[:-1])
print(word_4[-6:-3])
print(word_4[::-1])

# malcom_phrase = "La vida se abre camino"
# print(malcom_phrase[::2])
# # Imprime cada 3 valores empezando desde el 0 pero invierte la cadena
# print(malcom_phrase[::-3])

# # Conversion de cadenas
# value_1 = '1'
# print(id(value_1))
# print(id(int(value_1)))
# value_2 = 2
# value_3 = '2424.2342342'
# print(value_1 + str(value_2))
# print(int(value_1) + value_2)
# print(value_2 + float(value_3))

# # Reemplazar cadenas
# message = "Luke I am your mother!!!!"
# print(id(message))
# message = message.replace('mother', 'father')
# print(message)
# print(id(message))

# # Format expressions

# phrase_1 = "power"
# phrase_2 = "responsability"
# print('Whit great %s comes a great %s' % (phrase_1, phrase_2))
# print('Whit great {0} comes a great {1}'.format(phrase_1, phrase_2))
# print('Whit great {text_1} comes a great {text_2}'.format(
#     text_1=phrase_1, text_2=phrase_2))
# print(f'Whit great {phrase_1} comes a great {phrase_2}')
