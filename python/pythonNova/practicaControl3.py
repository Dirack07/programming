
programar = input("Sabes programar en python? [S/N]: ")
ingles = input("Sabes hablar en idioma ingles? [S/N]: ")

programar = programar.lower()
ingles = ingles.lower()

if programar == "s" and ingles == "s":
    print("Cumples con los requisitos para postularte")
elif programar == "s" and ingles == "n":
    print("Para postularte necesitas tener conocimientos en ingles")
elif programar == "n" and ingles == "s":
    print("Para postularte necesitas saber programar en python")
else:
    print("Para postularte, necesitas saber programar en python y tener conocimientos en ingles")
