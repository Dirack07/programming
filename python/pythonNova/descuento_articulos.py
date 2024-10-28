
for i in range(3):
    articulo = input("Ingresa nombre del articulo: ")
    clave = int(input("Ingresa clave del articulo [403 o 202]: "))
    precio = float(input("Ingresa precio del articulo: "))

    if clave == 403:
        descuento = precio * (10 / 100)
        precio_descuento = precio - descuento
        print("============================================================================================================================")
        print(
            f"Clave: {clave} | Nombre del articulo: {articulo} | Precio Original: {precio} | Precio con descuento: {precio_descuento}")
        print("============================================================================================================================")
    elif clave == 202:
        descuento = precio * (20 / 100)
        precio_descuento = precio - descuento
        print("============================================================================================================================")
        print(
            f"Clave: {clave} | Nombre del articulo: {articulo} | Precio Original: {precio} | Precio con descuento: {precio_descuento}")
        print("============================================================================================================================")
    else:
        print("============================================================================================================================")
        print("Clave incorrecta!!!")
        print("============================================================================================================================")
