#51. Programa que permita almacenar 10 valores en un vector que represente las edades de 10 
#personas y luego muestre cada uno de los valores ingresados. 

edades = [0] * 10

for i in range(10):
    edad = int(input("Digite la edad de la persona " + str(i + 1) + ": "))
    edades[i] = edad

print("\nEdades ingresadas:")
for i in range(10):
    print("Edad de la persona " + str(i + 1) + ": " + str(edades[i]))
