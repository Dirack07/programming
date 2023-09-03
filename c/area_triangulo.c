#include <stdio.h>
#include <math.h>

void area_triangulo(float *a, float *b, float *c, double *area){
    
    double s = (*a + *b + *c) / 2.0;
    *area = sqrt(s * (s - *a) * (s - *b) * (s - *c));

}

int main(void){

    float lado1, lado2, lado3;
    double area;

    printf("Hola!\n");
    printf("Programa que calcula el area de un tringulo\n");

    printf("Ingresa el tamanio del lado numero 1:\n");
    scanf("%f", &lado1);
    
    printf("Ingresa el tamanio del lado numero 2:\n");
    scanf("%f", &lado2);

    printf("Ingresa el tamanio del lado numero 3:\n");
    scanf("%f", &lado3);

    printf("Calculando area del triangulo...\n");

    area_triangulo(&lado1, &lado2, &lado3, &area);

    printf("El area del triangulo es: %f\n", area);

    return 0;
}