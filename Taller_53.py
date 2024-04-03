#

vector = [0] * 12

for i in range(12):
    num1 = int(input("Digite el numero para sumar " + str(i + 1) + ": "))
    vector[i] = num1

suma = 0
for num1 in vector:
    suma += num1

print("La suma de todos los valores es:", suma)
