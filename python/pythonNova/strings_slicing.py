# strings[start:stop:step]

# star = indice de inicio del substring (incluido)
# stop = indice del final del substring (no incluido)
# step = paso

saludo = "Hola David"
print(saludo[0:6])

print(saludo[3::3])

print(saludo[::-1])

texto = "Controlar la complejidad es la esencia de la programacion"
print(texto[0:9])


texto = "Nunca confies en un ordenador que no puedes lanzar por una ventana"
print(texto[8::3])

texto = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
print(texto[::-1])
