#Hacer el area y perímetro de un círculo
#área del círculo es pi*r^2
#el perímetro es 2 * pi * r
import math
#entradas
radio = float(input("Ingresa el radio del círculo: "))

#procesos
area = (math.pi) * pow(radio, 2)
perimetro = 2 * math.pi * radio


#salidas
print("El área del círculo es: ", round(area, 2))
print(f"El perímetro del circulo es: {round(perimetro, 2)}")
