

# Slicing de cadenas
word_4 = "Wayne is batman"
print(word_4[:8])
print(word_4[1:3])
print(word_4[4:])
print(word_4[:-1])
print(word_4[-6:-3])

malcom_phrase = "La vida se abre camino"
print(malcom_phrase[::-1])
print(malcom_phrase[::2])

# Conversion de cadenas
value_1 = '1'
value_2 = 2
value_3 = '2424.2342342'
# print(value_1 + str(value_2))
# print(int(value_1 + value_2))
# print(value_2 + float(value_3))

# Reemplazar cadenas
messages = "Luke I am your mother"
messages = messages.replace('mother', 'father')
print(messages)
print(repr(messages))

messages_2 = "La vida se abre camino"
print(messages_2.capitalize())
print(messages_2.upper())
print(messages_2.lower())
print(messages_2.find('vida'))


# Format expressions
phrase_1 = "power"
phrase_2 = "responsability"

print('Whit great %s comes a great %s' % (phrase_1, phrase_2))
print('Whit great {0} comes a great {1}'.format(phrase_1, phrase_2))
print('Whit great {text_1} comes a great {text_2}'.format(
    text_1=phrase_1, text_2=phrase_2))
print(f'Whit great {phrase_1} comes a great {phrase_2}')
