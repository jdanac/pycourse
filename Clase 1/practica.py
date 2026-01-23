# Práctica 1

# Ejercicio 1
# Pedir el nombre y el apellido al usuario y mostrar el nombre completo.
# Ejemplo
# Nombre: Luis
# Apellido: Pérez
# Salida: "Luis Pérez"

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_completo = nombre + " " + apellido
print("Nombre completo:", nombre_completo)

# Ejercicio 2
# Pedir dos números al usuario y mostrar la suma, resta, multiplicación y división.
# Ejemplo
# Número 1: 10
# Número 2: 5
# Salida:
# Suma: 15
# Resta: 5
# Multiplicación: 50
# División: 2.0

num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2
print("Suma:", suma)
print("Resta:", resta)
print("Multiplicación:", multiplicacion)
print("División:", division)

# Ejercicio 3
# Pedir la edad al usuario y calcular en qué año nació.
# Ejemplo
# Edad: 25
# Salida: "1999"

edad = int(input("Ingrese su edad: "))
año_actual = 2026
año_nacimiento = año_actual - edad
print("Año de nacimiento:", año_nacimiento)

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
cantidad = float(input("Ingrese la cantidad: "))
impuesto = 0.13
total_sin_imp = precio * cantidad
total_con_imp = total_sin_imp * (1 + impuesto)
print(cantidad, producto, total_con_imp)