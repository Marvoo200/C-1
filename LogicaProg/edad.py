#obtener la edad de la persona

#entradas
edad = int(input("Escribe tu edad: "))

#Procesos

if(edad >=18 and edad <= 120):
    print("Eres mayor de edad")
elif(edad <18 and edad >= 0):
    print("Eres menor de edad")
else: 
    print("nadie puede tener esa edad")

