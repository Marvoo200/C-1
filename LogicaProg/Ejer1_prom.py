#entradas

cal1 = float(input("Ingrese la calificacion 1: "))
cal2 = float(input("Ingrese la calificacion 2: "))
cal3 = float(input("Ingrese la calificacion 3: "))

#proceso

promedio = (cal1 + cal2 + cal3)/3

if(promedio > 6 and promedio <=10):
    print("Aprobaste con ", round(promedio, 2), " de promedio ^_^")
elif(promedio == 6):
    print("Pasaste de panzaso con 6 (:")
elif(promedio >= 0 and promedio < 6):
    print(f"Reprobaste ):{round(promedio, 2)}")
else:
    print("Error en el promedio :O")

#Salida


