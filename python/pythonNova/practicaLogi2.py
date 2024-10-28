# Verifica si las palabras almacenadas en las siguientes variables

# palabra1= "exito"
# palabra2="tecnologia"

# No se encuentran en la frase siguinte y almacena el resultado de esta comprobacion en una variables llamada mi_bool

# Cuando algo es lo suficientemente importante, lo haces incluso si las posibilidades de que salga bien no te acompanan


frase = "Cuando algo es lo suficientemente importante, lo haces incluso si las posibilidades de que salga bien no te acompanan"

palabra1 = "exito"
palabra2 = "tecnologia"

mi_bool = not palabra1 in frase and not palabra2 in frase
print(mi_bool)

mi_bool = palabra1 in frase
print(mi_bool)

mi_bool = palabra2 in frase
print(mi_bool)
