# ==========================================
# PROYECTO FINAL - BASE DE BATTLESHIP
# Curso: SOFT-302 – Introducción a la Programación
# ==========================================

import random

# --------------------------
# Emojis del juego
# --------------------------

def emoji_agua():
    return "🌊"

def emoji_explosion():
    return "💥"

def emoji_x():
    return "❌"


# --------------------------
# Crear tablero (lista simple)
# --------------------------

def crear_tablero(filas, columnas):
    tablero = []
    total_celdas = filas * columnas

    for _ in range(total_celdas):
        tablero.append(emoji_agua())

    return tablero


# --------------------------
# Mostrar tablero como cuadrícula
# --------------------------

def imprimir_tablero(tablero, columnas):
    contador = 0

    for celda in tablero:
        print(celda, end=" ")
        contador += 1

        if contador % columnas == 0:
            print()


# --------------------------
# Conversión fila/columna a índice
# --------------------------

def posicion_a_indice(fila, columna, columnas):
    return fila * columnas + columna


# --------------------------
# Colocar barcos aleatoriamente
# --------------------------

def colocar_barcos_aleatorios(tablero, cantidad_barcos):
    barcos = []
    total_posiciones = len(tablero)

    while len(barcos) < cantidad_barcos:
        posicion = random.randint(0, total_posiciones - 1)

        if posicion not in barcos:
            barcos.append(posicion)

    return barcos


# --------------------------
# Aplicar un disparo
# --------------------------

def disparar(tablero, indice, barcos):
    if indice in barcos:
        tablero[indice] = emoji_explosion()
        barcos.remove(indice)
        print("¡Impacto!")
    else:
        tablero[indice] = emoji_x()
        print("Agua...")


# --------------------------
# Programa principal
# --------------------------

# Pedir configuración del juego
filas = int(input("Digite la cantidad de filas: "))
columnas = int(input("Digite la cantidad de columnas: "))
cantidad_barcos = int(input("Digite la cantidad de barcos: "))

# Crear tablero
tablero = crear_tablero(filas, columnas)

# Colocar barcos
barcos = colocar_barcos_aleatorios(tablero, cantidad_barcos)

print("\nTABLERO INICIAL")
imprimir_tablero(tablero, columnas)

# Ejemplo de un disparo
print("\nDISPARO")

fila = int(input("Fila: "))
columna = int(input("Columna: "))

indice = posicion_a_indice(fila, columna, columnas)
disparar(tablero, indice, barcos)

print("\nTABLERO ACTUALIZADO")
imprimir_tablero(tablero, columnas)

