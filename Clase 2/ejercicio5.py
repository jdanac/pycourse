nombreProd = input("Introduzca el nombre del producto: ")
precioProd = int(input("Introduzca el precio del producto: "))

if precioProd > 50000:
    descuento = precioProd * 0.10
elif precioProd >= 25000:
    descuento = precioProd * 0.05
else:
    descuento = 0

precioFinal = precioProd - descuento

print("Producto:", nombreProd)
print("Precio original:", precioProd)
print("Descuento:", descuento)
print("Precio final:", precioFinal) 
