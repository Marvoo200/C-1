#Determinar la edad de una persona con el año actual y año de nacimiento
#entradas

nacimiento = int(input("Ingresa tu año de nacimiento: "))
año = int(input("Ingresa el año actual: "))

#procesos

edad = año - nacimiento

#salidas

print(f"Tienes {edad} años")
