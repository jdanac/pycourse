lista = []
prod = input("Ingrese un producto / ingrese fin para terminar: ")
precio = float(input("Ingrese el precio del producto: "))
limite = 'fin'
lista.append((prod, precio))
print(lista)

while limite != prod:
    prod = input("Ingrese un producto: ")
    if prod == limite:
        sum = 0
        for i in lista:
            sum += i[1]
        print(f"El total de la compra es: {sum}")
        break
    precio = float(input("Ingrese el precio del producto: "))
    lista.append((prod, precio))
    print(lista)


    