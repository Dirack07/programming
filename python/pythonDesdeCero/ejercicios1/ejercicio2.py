# 2. Escribe un programa que le pida primero su nombre al usuario, posteriormente
# su apellido, crea una variable de nombre completo concatenando el nombre y el
# apellido y muestra en pantalla un mensaje de bienvenida utilizando la variabla
# con el nombre completo.

nombre = input("Ingresa nombre: ")
apellido = input("Ingresa apellido: ")
nombre_completo = nombre + " " + apellido

print(f"Bienvenido {nombre_completo}")
