
print("Bienvenido al taller numero 22.")

#Hacer un codigo que permita calcular el valor final a pagar en una súper tienda.
prod1=int(input("Digite el precio del producto: "))
prod2=int(input("Digite el precio del producto: "))
prod3=int(input("Digite el precio del producto: "))
prod4=int(input("Digite el precio del producto: "))
prod5=int(input("Digite el precio del producto: "))

valortotal=prod1+prod2+prod3+prod4+prod5

#Por compras entre 10000 y 20000 el 10%.
if valortotal>=10000 and valortotal<=20000:
    descuento=valortotal*.10
    finaldescuento10=valortotal-descuento
    print("Este es el valor final con su descuento",finaldescuento10)
#Por compras entre 20001 y 50000 el 30%
elif valortotal>20000 and valortotal <=50000:
    descuento2=valortotal*.30
    fianldescuento30=valortotal-descuento2
    print("Este es el valor final con su descuento",fianldescuento30)
#Por compras superiores a 50000 el 50%
elif valortotal>50000:
    descuento3=valortotal*.50
    valordescuento50=valortotal-descuento3
    print("Este es el valor final con su descuento",valordescuento50)
else:
    descuento=0
