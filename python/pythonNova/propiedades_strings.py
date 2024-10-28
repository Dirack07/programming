# Son inmutables: no pueden modificar sus partes pero si pueden reasignarse los valores a traves de metodos strings

# Concatenables: es posible unir con el simbolo +

# Multiplicables: es posible concatenar repeticiones de un string con el simbolo +

# Determinar su logitud: a traves de la funcion len(string)

# verificar su contenido: a traves de las palabras clave in y not in, el resultado de esta sera booleano (True/False)

nombre = "Carina"
# nombre[0] = "K" # Error no se pueden cambiar los strings
# print(nombre)

n1 = "Kari"
n2 = "na"
print(n1+n2)
print(n1*10)

poema = "Mil pequenos peces blancos como si hirviera el color del agua"
print(poema)

print("agua" in poema)

print("sol" in poema)

print("sol" not in poema)

print("agua" in poema)

print(len(poema))
