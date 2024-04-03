#66. Programa que permita llenar una matriz cuyo número de filas y columnas es ingresado por 
#el usuario, donde se busque un valor (Ingresado por el usuario) y al encontrarlo muestre su posición 
#(fila, columna).

def mostrar_valor(matriz, filas, columnas, valor_buscado):
  encontrado = False
  for i in range(filas):
    for j in range(columnas):
      if matriz[i][j] == valor_buscado:
        encontrado = True
        print(f"El valor {valor_buscado} se encuentra en la posición ({i + 1}, {j + 1})")
        break
    if encontrado:
      break

def main():
  while True:
    try:
      filas = int(input("Digite el número de filas: "))
      columnas = int(input("Digite el número de columnas: "))
      if filas > 0 and columnas > 0:
        break
      else:
        print("Las filas y columnas deben ser números positivos.")
    except ValueError:
      print("Valor inválido. Ingrese un número entero.")

  matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

  for i in range(filas):
    for j in range(columnas):
      valor = int(input(f"Digite el valor para la posición ({i}, {j}): "))
      matriz[i][j] = valor

  valor_buscado = int(input("Digite el valor a buscar: "))

  mostrar_valor(matriz, filas, columnas, valor_buscado)

if __name__ == "__main__":
  main()
