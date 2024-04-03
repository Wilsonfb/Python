#62. Programa que permita llenar una matriz y mostrar todos los datos ingresados y su respectiva 
#posición (fila, columna) en pantalla 

def mostrar_matriz(matriz):
  
  filas = len(matriz)
  columnas = len(matriz[0])
  
  for i in range(filas):
    for j in range(columnas):
      print(f"({i}, {j}): {matriz[i][j]}", end=" ")
    print()

def main():
 
  filas = int(input("Digite el número de filas: "))
  columnas = int(input("Digite el número de columnas: "))

  matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

  for i in range(filas):
    for j in range(columnas):
      valor = input(f"Ingrese el valor para la posición ({i}, {j}): ")
      matriz[i][j] = valor

  mostrar_matriz(matriz)

if __name__ == "__main__":
  main()
