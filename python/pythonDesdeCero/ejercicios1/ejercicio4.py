# 4. Escribe un programa que al proporcionarle la siguiente clave HomeroSimpson1970SpringfieldUSA
# nos guarde el nombre, apellido, año, estado y país en variables independientes y
# porteriormente muestra en pantalla un mensaje de bienvenida utilizando las variables.

clave = input("Ingresa la clave: ")
nombre = clave[0:6]
apellido = clave[6:13]
anio = clave[13:17]
estado = clave[17:28]
pais = clave[28:]
print(
    f"""
    Hola bienvenido! 
    
    Nombre: {nombre}
    Apellido: {apellido}
    Anio: {anio}
    Estado: {estado}
    Pais: {pais}
""")
