

edad = int(input("Ingresa tu edad: "))


if edad >= 18:
    licencia = input("Tienes licencia de conducir? [S/N]: ")
    if licencia == "S":
        print("Puedes conducir: ")
    else:
        print("No puedes conducir necesitas una licencia")
else:
    print("No puedes conducir aun. Debes tener 18 anios y contar con una licencia.")
