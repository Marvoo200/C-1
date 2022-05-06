#Hacer un calculo de salario 

#Entradas


mes = input("Ingresa el mes: ")
dias = int(input("Ingresa los días que tiene el mes: "))
pago = float(input("Ingresa el pago por día: "))

#Proceso

pago_base = dias * pago
iva_traslado = pago_base * 0.16
subtotal = pago_base * 1.16
iva_retenido = 2/3 * iva_traslado
isr_retenido = pago_base * 0.10
pago_neto = subtotal - iva_retenido - isr_retenido


#Salida
print("mes: ", mes, "\nDías laborables: ", dias, "\nPago por día: $", pago, 
    "\nPago base: $", round(pago_base, 2), "\nIVA traslado: $", round(iva_traslado, 2), "\nSubtotal: $", round(subtotal, 2),
    "\nIVA retenido: $", round(iva_retenido, 2), "\nISR retenido: $", round(isr_retenido, 2), "\nPago neto: $", round(pago_neto, 2))
