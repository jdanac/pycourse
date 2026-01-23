# Ejercicio 4
# Pedir al usuario un nombre de un producto, su precio y la cantidad que desea comprar.
# Calcular el total a pagar incluyendo un impuesto del 13%.
# Ejemplo
# Producto: Camisa
# Precio: 20.00
# Cantidad: 2
# Salida: "Total a pagar por 2 Camisas es: 45.20

producto = input("Ingrese el producto: ")
precio = float(input("Ingrese el precio: "))
cantidad = int(input("Ingrese la cantidad: "))
impuesto = 0.13
total_sin_imp = precio * cantidad
total_con_imp = total_sin_imp * (1 + impuesto)
print("El total a pagar por", cantidad, producto +"s", "es:", total_con_imp)