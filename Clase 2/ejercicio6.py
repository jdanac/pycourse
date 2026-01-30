nombre = input("Introduzca su nombre: ")
salarioBruto = int(input("Introduzca su salario bruto mensual en CRC: "))

deducciones = salarioBruto * 11.83 / 100

if salarioBruto > 4727000:
    renta = (salarioBruto - 4727000) * 0.25
elif salarioBruto >= 2364000:
    renta = (salarioBruto - 2364000) * 0.20
elif salarioBruto >= 1347000:
    renta = (salarioBruto - 1347000) * 0.15
elif salarioBruto > 918000:
    renta = (salarioBruto - 918000) * 0.10
else:
    renta = 0

print('Salario Bruto en CRC:', salarioBruto)

print('Base imponible (11.83%):', deducciones)
print('Impuesto al salario:', renta)
print('Total de deducciones:', deducciones + renta)

salarioNeto = salarioBruto - deducciones - renta
print('Salario Neto en CRC:', salarioNeto)