from decimal import *

# Numeros en python

# Enteros
integer_number = 1
print(type(integer_number))

binary_number = 0b1010101111101010
print(type(binary_number))

octal_number = 0o145323467
print(type(octal_number))

hex_number = 0x345345abcdef
print(type(hex_number))

# A partir de python 3.6 se puede hacer esto
num = 1_234_5424_34_3
print(num)
print(type(num))

# Si te encuentras un valor numerico demasiado grande
# Para las capacidades de python
# inf infinito
# non not a number

# Flotantes
float_number = 535534.554
print(type(float_number))

float_number2 = 2E10
print(float_number2)
print(type(float_number2))

# Errores con flotantes
a = 0.1
b = 0.2
print(a+b)

a = 1.2
b = 1.0
print(a-b)

# Decimal
D = Decimal
decimal_number = D('1.24')
print(type(decimal_number))

# Crear decimales de flotantes no es recomendado
decimal_number2 = D('242342.2323')
print(type(decimal_number2))

a = D('0.1')
b = D('0.2')
print(a+b)

getcontext().prec = 2
print(D('1') / D('7'))

print(getcontext())
