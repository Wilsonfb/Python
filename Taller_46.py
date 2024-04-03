#46. Programa que permita calcular el valor a pagar en una caja registradora donde se reciben N productos y se ingresan los precios de uno en uno.

cantidad= int(input("Cuantos productos van a pagar: "))
i = 0
lista = []
while i < cantidad:
    producto = float(input("Digite el valor del producto: "))
    i +=1
    lista.append(producto)

total = sum(lista)

print(f"El total es de {total:.3f}.")
