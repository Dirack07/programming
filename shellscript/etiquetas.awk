{
    etiqueta = $1
    valor1 = $2
    valor2 = $3

    datos[etiqueta] = datos[etiqueta] valor1 " " valor2 "\n"
} END {
    for (etiqueta in datos) {
        printf("%s %s", etiqueta, datos[etiqueta])
    }
}
