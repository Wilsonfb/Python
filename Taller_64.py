#64. Programa que permita llenar una matriz cuyo número de filas y número de columnas es 
#ingresado por el usuario. Se le debe luego preguntar al usuario que posición de la matriz desea ver 
#(que fila y que columna) y mostrar el contenido de esa posición. Se debe repetir la pregunta tantas 
#veces sea necesario hasta que el usuario solicite un numero de fila o número de columna mayor al 
#asignado a la matriz. 

def mostrar_valor(matriz, filas, columnas):

  while True:
    try:
      fila = int(input("Digite la fila (1-{} ): ".format(filas)))
      columna = int(input("Digite la columna (1-{} ): ".format(columnas)))

      if 1 <= fila <= filas and 1 <= columna <= columnas:

        valor = matriz[fila - 1][columna - 1]
        print(f"El valor en la posición ({fila}, {columna}) es: {valor}")
        break
      else:
        print("Posición fuera de rango. Intente de nuevo.")
    except ValueError:
      print("Valor inválido. Digite un número entero.")

def main():
 
  filas = int(input("Digite el número de filas: "))
  columnas = int(input("Digite el número de columnas: "))

  matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

  for i in range(filas):
    for j in range(columnas):
      valor = input(f"Digite el valor para la posición ({i}, {j}): ")
      matriz[i][j] = valor

  mostrar_valor(matriz, filas, columnas)

if __name__ == "__main__":
  main()
