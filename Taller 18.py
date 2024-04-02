#Determinar cuánto pagara una persona por una compra.

print("Bienvenido al taller numero 18.")

#Codigo para ver la cantidad de articulos y el valor.

cantidadarti=int(input("Cuantos productos estan llevando: "))
valor=int(input("Introdusca el valor unitario de cada producto: "))
total=valor*cantidadarti
totaldeldescuento=total*.20

#Codigo de descuento del 20% de una compra superior a 100000.

if total>=100000:
    totaldeldescuento=total*.20
    totalfinal=total-totaldeldescuento
    print("El valor total segun el 20% de su descuento es:",totalfinal)
else:
    print("El valor que debe pagor sin el descuento es:",total)
