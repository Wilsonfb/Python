#55. Programa que permita llenar un vector de 20 posiciones y luego le pregunte al usuario cual 
#posición desea ver en pantalla. 

vector = []

for i in range(20):
    valor = input(f"Ingrese el valor para la posición {i + 1}: ")
    vector.append(valor)

while True:
    posicion = int(input("Ingrese la posición que desea ver en pantalla (1-20), o un número mayor para salir: "))
    if 1 <= posicion <= 20:
        print(f"El valor en la posición {posicion} es: {vector[posicion - 1]}")
    else:
        print("Posición fuera de rango. ¡Adiós!")
        break
    
