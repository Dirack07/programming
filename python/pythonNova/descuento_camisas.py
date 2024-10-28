
contador = 0
continuar = "Y"
precio_camisa = 0
total = 0

while continuar == "Y":
    contador += 1
    print(f"Camisa numero: {contador}")
    precio_camisa = float(input("Ingrese el precio de la camisa: "))
    total += precio_camisa
    continuar = input("Continuar [Y/n]: ")

if contador >= 3:
    descuento = total * (15 / 100)
    precio_descuento = total - descuento
    print("============================================================================================================================")
    print(
        f"Precio Original: {total} | Precio con descuento: {precio_descuento}")
    print("============================================================================================================================")
else:
    descuento = total * (3 / 100)
    precio_descuento = total - descuento
    print("============================================================================================================================")
    print(
        f"Precio Original: {total} | Precio con descuento: {precio_descuento}")
    print("============================================================================================================================")
