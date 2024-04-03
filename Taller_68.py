#68. Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por 
#el usuario y luego calcule la suma de cada una de sus columnas (una x una) 

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

sum_f = int(input("Que fila quiere sumar: "))
suma = 0

for row_position in range(rows):
    for elements in range(columns):
        if (row_position==(sum_f-1)):
            print(matriz[row_position][elements])
            suma += matriz[row_position][elements]
print (f"La suma de la fila {row_position} es {suma}")
