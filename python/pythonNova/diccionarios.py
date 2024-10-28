# Los diccionarios son estructuras de datos que almacenan informacion en pares clave:valor

# Son especialmente utiles para guardar y recuperar informacion a partir de los nombres de sus claves (NO UTILIZA INDICES)

# Se escribe entre llaves y s eseparan por comas

# Las claves y su valor separada por dos puntos

mi_diccionario = {"Curso": "Python", "Clae": "Diccionarios"}
# Keys
# Values
# Items

diccionario = {"c1": "valor1", "c2": "valor2"}
print(type(diccionario))

diccionario = {"c1": "valor1", "c2": "valor2"}
resultado = diccionario["c1"]
print(resultado)

cliente = {"nombre": "Juan", "apellido": "Fuentes", "peso": 88, "altura": 1.86}
consulta = cliente["apellido"]
print(consulta)

dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(dic["c2"][1])

dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(dic["c3"])

dic = {"c1": 55, "c2": [10, 20, 30], "c3": {"s1": 100, "s2": 200}}
print(dic["c3"]["s2"])

dic = {"c1": ["a", "b", "c"], "c2": ["d", "e", "f"]}
print(dic["c2"][1].upper())

dic = {1: "a", 2: "b"}
print(dic)
dic[3] = "c"
print(dic)

dic = {1: "a", 2: "b"}
print(dic)
dic[3] = "c"
print(dic)
dic[2] = "B"
print(dic)

print(dic.keys())
print(dic.values())
print(dic.items())
