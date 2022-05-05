#Obtener X1 y X2 con la formula general

import math
#Entradas

a = float(input("Ingrese el valor de A: "))
b = float(input("Ingrese el valor de B: "))
c = float(input("Ingrese el valor de C: "))

#Proceso

x1 = (-b-(math.sqrt((math.pow(b, 2) - 4 * a * c))))/(2*a)

x2 = (-b+(math.sqrt((math.pow(b, 2) - 4 * a * c))))/(2*a)

#Salidas

print("X1 = ", round(x1, 4))
print("X2 = ", round(x2, 4))

