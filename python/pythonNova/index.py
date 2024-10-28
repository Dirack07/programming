# Utilizamos el metodo index() para explorar strings ya que permite hallar el indice de aparicion de un caracter o cadena dentro de un texti dado
# En python el indice empeza en 0

# mi_texto = "Esta es una prueba"
# resultado = mi_texto[0]
# print(resultado)

# resultado = mi_texto[-4]
# print(resultado)

# resutado = mi_texto.index("n")
# print(resultado)

# resultado = mi_texto.index("prueba")
# print(resultado)

# resultado = mi_texto.index("a")
# print(resultado)

# resultado = mi_texto.index("a", 5)
# print(resultado)

# resultado = mi_texto.rindex("a")
# print(resultado)

# resultado = mi_texto.index("prueba")
# print(resultado)

# mi_texto = "Ordenador"
# resultado = mi_texto[4]
# print(resultado)


mi_texto = "En teroia, la teoria y la practica son los mismos. En la practica no lo son"
resultado = mi_texto.index("practica")
print(resultado)

mi_texto = "En teroia, la teoria y la practica son los mismos. En la practica no lo son"
resultado = mi_texto.rindex("practica")
print(resultado)
