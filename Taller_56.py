#56. Programa que permita llenar un vector de 18 posiciones y después mostrarlo al revés.

vector = []

for i in range(18):
    num = int(input("Digite un numero: "))
    vector.append(num)

invertida = list(reversed(vector))

print(invertida)
