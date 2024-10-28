import re

listadenombres = ["Marco", "Laura", "monica", "Javier",
                  "Celina", "Martha", "Dario", "Emiliano", "Melisa"]

for indice, nombre in enumerate(listadenombres):
    print(f"{nombre} se encuentra en el indice {indice}")


lista_indices = list(enumerate("Python"))
print(lista_indices)


lista_nombres = ["Crsitian", "Daya", "Marifer", "Juan Carlos",
                 "Claudia", "Megan", "David", "Yolanda", "Matias"]

for indice, nombre in enumerate(lista_nombres):

    # n = re.search("^M", nombre)
    if re.search("^C", nombre):
        print(nombre)
    else:
        pass
