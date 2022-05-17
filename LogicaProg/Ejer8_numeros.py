'''
Obtener un número y determinar lo siguiente:
a) si es negativo y mayor a -100 imprimir los números impares de forma DESCENDENTE
b) si es positivo y menor a 100 mostrar los números pares de forma ASCENDENTE
c) en otro caso imprimir No Válido
'''


#entradas

num = int(input("Ingresa el numero: "))

#Proceso

if(num < 100 and num > 0):
    for i in range(1, num+1):
        if(i %2 == 0):
            print(i)
elif(num<0 and num >-100):
    for i in range (0, num-1, -1):
        if (i %2 !=0 and num < 0):
            print(i)
else:
    print("Numero invalido, solo se puede de -100 a 100")

#Salidas

    
    
    

