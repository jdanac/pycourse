contador = int(input("Ingrese cuantas notas desea calcular: "))
notas = []
for i in range(contador):
    nota = float(input("Ingrese las notas: "))
    notas.append(nota)

promedio = sum(notas) / contador

print("Las notas ingresadas son:", notas)
print("El promedio de las notas es:", promedio)