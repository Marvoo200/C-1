#Importar las librerias
#librería math para funciones matematicas

import math 


#Entradas
#definir las variables de entrada



numero_1 = float(input("Ingresa un número: "))
numero_2 = float(input("Ingresa otro número: "))

#Procesos (cálculos u operaciones)
suma = numero_1 + numero_2
resta = numero_1 - numero_2
multiplicacion = numero_1 * numero_2
division = numero_1 / numero_2

potencia_1 = numero_1 ** numero_2
potencia_2 = pow(numero_1, numero_2)
cuadrado = numero_1 ** 2
cubo = pow(numero_2, 3)


raiz_cuadrada_1 = pow(9, 1/2)
raiz_cuadrada_2 = math.sqrt(9)
raiz_cubica = pow(27, 1/3)

modulo_residuo = numero_1 % numero_2

#salidas

print("La suma es: ", suma)
print("La resta es: ", resta)
print("La multiplicacion es: ", multiplicacion)
print("La division es: ", division)

print("la potencia 1 es: ", potencia_1)
print("La potencia 2 es: ", potencia_2)
print("El cuadrado es: ", cuadrado)
print("El cubo es: ", cubo)
print("La raíz cuadrada 1 es: ", raiz_cuadrada_1)
print("La raíz cuadrada 2 es: ", raiz_cuadrada_2)
print("La raíz cúbica es: ", raiz_cubica)

print("El modulo o residuo es: ", modulo_residuo)

