# Asignacion de variables

# Basica
batman = "Bruce"

# Asignacion por tupla
batman, butler = 'Bruce', 'Alfred'
print(batman)
print(butler)

# Asignacion por lista
[batman, butler] = ['Bruce', 'Alfred']
print(batman)
print(butler)

# Asignacion por secuencia
# los strings son secuencias inmutables
a, b, c, d, e, f, g, h = 'Catwoman'
print(c)

# Extended sequence unpacking
a, *b = 'Batman'
print(f"Valor de variable a: {a}")
print(f"Valor de variable b: {b}")

# Multiple target Asignment
batman = senorito_wayne = 'Bruce'
print(batman)
print(senorito_wayne)

# Asignacion aumentada
# batman += ' es Patinson'
# print(batman)

batman = batman + ' es Patinson'
print(batman)
