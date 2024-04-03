#67. Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por 
#el usuario y luego calcule la suma de cada una de sus filas (una x una) 

rows = int(input("Cuantas filas quiere en la matriz: "))
columns = int(input("Cuantas columnas quiere en la matriz: "))

matriz = []

for row_position in range(rows):
    row = []
    for elements in range(columns):
        row.append(int(input(f"Elemento de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)

for row_position in range(rows):
    suma_fila = sum(matriz[row_position])
    print(f"La suma de la fila {row_position} es {suma_fila}.")
