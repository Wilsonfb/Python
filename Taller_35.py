#35.Programa que muestre en pantalla los múltiplos de 3 teniendo como límite el número 99.

mult = []

for i in range(100):
    if i % 3 == 0:
        mult.append(i)
print(mult)
