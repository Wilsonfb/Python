#37. Realizar un Programa que permita visualizar en pantalla los múltiplos de 5 hasta el número 100.

multiplos = []

for i in range(1,101):
    if i%5==0:
        multiplos.append(i)
print(multiplos)
