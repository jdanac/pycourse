# Ciclo while -> Repite un bloque de código mientras una condición sea verdadera
# Podría ejecutarse indefinidamente si la condición nunca llega a ser falsa
# contador = 0
# while contador < 100:
#     contador = contador + 1
#     print("El contador vale:", contador)

# print("Terminé!")

# contador = 100
# for i in range(0, contador + 1, 1):
#     print('Número:', i)

# print('Terminé')


# # # Ejemplo de ciclo que itera sobre las letras de un texto
# texto = input("Ingrese un texto: ")
# contador = 0
# limite = len(texto)
# while contador < limite:
#     letra = texto[contador]
#     print("La letra en la posición", contador, "es:", letra)
#     contador = contador + 1

# texto = input('Ingrese una palabra: ')
# limite = len(texto)
# print(limite)
# for i in range(0, limite, 1):
#     letra = texto[i]
#     print('Letra en posición', i, 'es', letra)

# # Ejemplo de ciclo que revierta una palabra.
# # hola -> aloh
# palabra = input("Ingrese una palabra: ")
# contador = len(palabra) - 1
# limite = 0
# palabra_invertida = ""
# while contador > limite:
#     letra = palabra[contador]
#     palabra_invertida = palabra_invertida + letra
#     contador = contador - 1

# print("La palabra invertida es:", palabra_invertida)

# palabra = "hola"
# contador = 4
# palabra[contador - 1] -> palabra[3] -> "a"
# contador = 4 - 1 = 3
# palabra[contador - 1] -> palabra[2] -> "l"

palabra = input("Ingrese una palabra: ")
palabra_invertida = ""

for i in range(len(palabra) -1, -1, -1):
    letra = palabra[i]
    palabra_invertida = palabra_invertida + letra

print("La palabra invertida es:", palabra_invertida)
    

