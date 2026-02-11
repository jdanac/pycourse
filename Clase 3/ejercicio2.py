num = int(input("Ingrese un número: "))

contador = 1
while contador < 10:
    multi = num * contador
    contador = contador + 1
    print("El número multiplicado por", contador - 1, "es:", multi)

