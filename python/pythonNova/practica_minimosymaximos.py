lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475,
                 121676, 6654067, 353254, 123134, 55**12, 611**5]

valor_maximo = max(lista_numeros)
print(valor_maximo)

lista_numero = [44542247, 21310, 2134747, 44556475,
                121676, 6654067, 353254, 123134, 552512, 611665]

rango = max(lista_numero)-min(lista_numero)

print(max(lista_numero))
print(min(lista_numero))
print(rango)


diccionario_edades = {"Carlos": 55, "Maria": 42, "Mabel": 78, "Jose": 44,
                      "Lucas": 24, "Rocio": 35, "Sebastian": 19, "Catalina": 2, "Dario": 49}

edad_minima = min(diccionario_edades.values())
print(f"Edad minima: {edad_minima}")

ultimo_nombre = max(diccionario_edades.keys())
print(f"Ultimo nombre en orden alfabetico: {ultimo_nombre}")
