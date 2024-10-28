# Crear un diccionario mi_dic que almacene la siguiente informacion

my_dict = {"nombre": "Karen", "apellido": "Polo",
           "edad": 35, "ocupacion": "Periodista"}
print(my_dict)


# Crear una funcion print que devuelva del segundo item la lista llamada "points2" dentro del siguiente diccionario

my_dict = {"valores_1": {"v1": 3, "v2": 6}, "puntos": {
    "points1": 9, "points2": [10, 300, 15]}}
print(my_dict["puntos"]["points2"][1])

# Actualiza la informacion de nuestro diccionario llamado mi_dict (Reasignando nuevo valores a las claves segun correspondan)

my_dict = {"nombre": "Karen", "apellido": "Polo",
           "edad": 35, "ocupacion": "Periodista"}
print(my_dict)
my_dict["edad"] = 36
print(my_dict)
my_dict["ocupacion"] = "programadora"
my_dict["pais"] = "colombia"
print(my_dict)
