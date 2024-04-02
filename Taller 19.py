#Determinar el total a pagar por una compra.

print("Bienvenido al taller numero 19.")

#Hacer un codigo que permita resgistrar el valor unitario y la cantidad.

valor=int(input("Introdusca el valor unitario de cada producto: "))
cantidadarti=int(input("Cuantos productos estan llevando: "))
total=valor*cantidadarti
totalde15=total*.15
totalde35=total*.35

#Hacer un codigo para sacar el 15% o el 35% de una compra.

if total<=20000:
    totalde15=total*.15
    totalfinal15=total-totalde15
    print("El valor total segun el 15% del descuento es:",totalfinal15)
elif total>=20000:
    totalde35=total*.35
    totalfinalde35=total-totalde35
    print("El valor total segun el 35% de descuentoes:",totalfinalde35)
    