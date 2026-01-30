num1 = input("Introduzca el primer número: ")
num2 = input("Introduzca el segundo número: ")

if int(num1) > int(num2):
    print(num1, "es mayor que", num2)
elif int(num1) == int(num2):
    print(num1, "es igual a", num2)
else:
    print(num1, "es menor que", num2)