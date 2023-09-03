#include <stdio.h>

int main()
{
    //reglas de nombres de variables en compile
    //1.Es sensible a mayucaulas y minusculas
    //2.No podemos usar palabras reservadas
    //3.Como bunea practica usar notacion de camello
    //4.Debe iniciar con letras o con _
    //5.No debe iniciar con numeros o caracteres especiales
    //6.Despues del primer caracter podemos usar _, letras o numeros
    //7.Los nombres no pueden contener espacios en blanco
    //8.Se recomienda usar nombres descriptivos
    
    int miNumero2 = 20, miNumero3 = 30;// Como buena practica usar minusculas al inicio del nombre de una variable
    
    printf("Mi numero tres es %d\n, mi numero dos es %d", miNumero3, miNumero2);

    return 0;
}