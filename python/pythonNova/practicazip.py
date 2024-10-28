
paises = ["Alemania", "Japon", "Francia", "Finlandia", "Canada", "Australia"]
capitales = ["Berlin", "Tokio", "Paris", "Helsinski", "Ottawa", "Canverra"]

for pais, capital in zip(paises, capitales):
    print(f"La capital de {pais} es {capital}")


productos = ["Libretas", "Tenis", "Mouse"]
marcas = ["Scribe", "Nike", "Logitech"]

mi_zip = list(zip(productos, marcas))
print(mi_zip)

es = ["uno", "dos", "tres", "cuatro", "cinco"]
pt = ["um", "dois", "tres", "quatro", "cinco"]
en = ["one", "two", "three", "four", "five"]

zip_traducciones = list(zip(es, pt, en))
print(zip_traducciones)
