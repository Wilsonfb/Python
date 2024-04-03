#65. Programa que permita llenar un matriz cuyo número de filas y columnas es ingresado por el 
#usuario y luego determine cuantos números positivos, negativos y ceros fueron ingresaron 

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
  while True:
    try:
      filas = int(input("digite el número de filas: "))
      columnas = int(input("Digite el número de columnas: "))
      if filas > 0 and columnas > 0:
        break
      else:
        print("Las filas y columnas deben ser números positivos.")
    except ValueError:
      print("Valor inválido. Digite un número entero.")

  matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

  positivos = []
  negativos = []
  ceros = []

  for i in range(filas):
    for j in range(columnas):
      while True:
        try:
          valor = int(input(f"Digite el valor para la posición ({i}, {j}): "))
          break
        except ValueError:
          print("Valor inválido. Digite un número entero.")

      matriz[i][j] = valor

      if valor > 0:
        positivos.append((i, j))
      elif valor < 0:
        negativos.append((i, j))
      else:
        ceros.append((i, j))

  print(f"Positivos ({len(positivos)}):", positivos)
  print(f"Negativos ({len(negativos)}):", negativos)
  print(f"Ceros ({len(ceros)}):", ceros)

if __name__ == "__main__":
  main()
