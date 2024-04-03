#69. Programa que permita llenar una matriz cuadrada de 5 filas y 5 columnas y luego calcule la 
#suma de su diagonal principal. La diagonal principal de una matriz cuadrada es aquella donde el 
#número de fila es igual al número de columna) 

matriz = []

for row_position in range(5):
    row = []
    for elements in range(5):
        row.append(int(input(f"Elemento de la fila {row_position}: ")))
    matriz.append(row)

for row in matriz:
    print(row)

suma = 0

for row_position in range(5):
    suma += matriz[row_position][row_position]

print(f"La suma de la diagonal es {suma}.")
