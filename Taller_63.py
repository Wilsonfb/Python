#63. Programa que permita llenar una matriz de 3 filas y 4 columnas y luego determine: a) La 
#suma total de todos lo valores b) El valor promedio de todos los valores ingresados 

def main():
  
  filas = 3
  columnas = 4

  matriz = [[0 for _ in range(columnas)] for _ in range(filas)]

  for i in range(filas):
    for j in range(columnas):
      valor = int(input(f"Digite el valor para la posición ({i}, {j}): "))
      matriz[i][j] = valor

  suma = 0
  for i in range(filas):
    for j in range(columnas):
      suma += matriz[i][j]

  promedio = suma / (filas * columnas)

  print(f"Suma: {suma}.")
  print(f"Promedio: {promedio}.")

if __name__ == "__main__":
  main()
