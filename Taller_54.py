#

vector = [0] * 20

for i in range(20):
    num1 = float(input("Ingrese un numero " + str(i + 1) + ": "))
    vector[i] = num1

positivos = 0
negativos = 0
ceros = 0

for num1 in vector:
    if num1 > 0:
        positivos += 1
    elif num1 < 0:
        negativos += 1
    else:
        ceros += 1

print("Positivos:", positivos,".")
print("Negativos:", negativos,".")
print("Ceros:", ceros,".")