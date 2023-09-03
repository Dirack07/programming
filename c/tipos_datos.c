#include <stdio.h>
#include <stdbool.h>

int main()
{
    
    // Tipo entero formato %d, %i
    int entero = 10;
    printf("Tipo entero: %i\n", entero);
    
    //Tipo flotante formato %formato
    float flotante = 15.5;
    printf("Tipo flotante: %.1f\n", flotante);
    
    //Tipo double formato %lf -> long float
    double doble = 13.3;
    printf("Tipo doble: %.2lf\n", doble);
    
    //Tipo caracter formato %c
    char caracter = 'A';
    printf("Tipo caracter: %c\n", caracter);
    printf("Valor decimal caracter: %d\n", caracter);
    char carcacterDecimal = 65;
    printf("Tipo caracter decimal: %c\n", carcacterDecimal);
    
    //Tipo bool valores true 1 or false 0
    bool logico = true;
    printf("Tipo logico: %d\n", logico);
    
    //Arreglo es un conjunto de datos
    //Se encuentran ubicados de forma consecutiva en la memoria
    //Tipo cadena formato %s
    char cadena[] = "Hola";
    printf("Tipo cadena: %s\n", cadena);
    
    //Tipo cadena
    char cadena2[8] = "Saludos";
    printf("Tipo cadena 2: %s\n", cadena2);
    
    
    return 0;
}