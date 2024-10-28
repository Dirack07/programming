# Los operadores logicos permiten tomar decisiones basadas en multiples condiciones
# AND devuelve TRUE si todas las condiciones son verdaderas
a = 6 > 5
b = 30 == 15*3

mi_bool = a and b
print(mi_bool)


# OR devulve TRUE si al menos una condicion es verdadera
mi_bool = a or b
print(mi_bool)

# NOT devulve TRUE si el valor booleano es FALSE, y devulve FALSE si es TRUE

mi_bool = not a
print(mi_bool)
