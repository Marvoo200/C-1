#pedir un valor y obtener la temperatura
#conversion de grados de temperatura
#pedir una cantidad en grados y sustituir la variable azul

#entradas
grados = float(input("Ingresa los grados: "))

#proceso

celsius_1 = grados - 273.15 #kelvin a celsius
celsius_2 = (5*(grados-32))/9 #farenheit a celsius
kelvin_1 = grados + 273.15 #Celsius a kelvin
kelvin_2 = (5*(grados-32))/9 + 273.15 #farenheit a kelvin
farenheit_1 = (9*(grados-273.15))/5 + 32 # kelvin a farenheit
farenheit_2 = (9 * grados) / 5 + 32 # celcius a farenheit

#salida

print("Si ingresaste los grados en celcius las conversiones son las siguientes: ")
print(f"{grados} °C = {round(farenheit_2, 2)} °F")
print(f"{grados} °C = {round(kelvin_1, 2)} °K")
print("Si ingresaste los grados en farenheit las conversiones son las siguientes: ")
print(f"{grados} °F = {round(celsius_2, 2)} °C")
print(f"{grados} °F = {round(kelvin_2, 2)} °K")
print("Si ingresaste los grados en Kelvin las conversiones son las siguientes: ")
print(f"{grados} °K = {round(celsius_1, 2)} °C")
print(f"{grados} °K = {round(farenheit_1, 2)} °F")