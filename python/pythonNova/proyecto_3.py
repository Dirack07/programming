# Vamos a crear un programa que le pida al usaurio ingresar un texto
# El programa le va a pedir el usuario que ingrese 3 letras a su eleccion
# 1. Cuantas veces aparece cada una de las letras que eligio?
# 2. Le diras al usuario cuantas palabras hay a lo largo de todo el texto
# 3. Nos va a informar cual es la primera letra del texto y cual es la ultima
# 4. El sistema nos mostrara como quedariael texto si inviertieramos el orden de las palabras
# 5. El sistema nos va a decir si la palabra Python se encuentra dentro del texto

texto = input("Ingresa un texto: ")
letras = input("Ingresa tres letras: ")
letras = list(letras)
print(letras)

letra1 = texto.count(letras[0])
letra2 = texto.count(letras[1])
letra3 = texto.count(letras[2])

print(f"La primera letra se reprite: {letra1}")
print(f"La segunda letra se reprite: {letra2}")
print(f"La tercera letra se reprite: {letra3}")

palabras = len(texto.split())
print(f"El numero de palabras en el texto es: {palabras}")

primera_letra = texto[0:1]
print(f"La primera letra del texto es: {primera_letra}")
ultima_letra = texto[-1]
print(f"La ultima letra del texto es: {ultima_letra}")

print(texto[::-1])

resultado = "Python" in texto
print(f"La plabra 'python' se encuentra en el texto: {resultado}")
