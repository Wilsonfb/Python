# Programa que permita ingresar N números y determine cuantas veces aparece el mismo número, 
#dicho número a buscar debe solicitarse al usuario al inicio del programa. 

numeros = []

nueva_numero = int
while nueva_numero != 0:
    nueva_numero = int(input("Introduce los numeros que quieras, y si quieres salir del prograa preciona cero: "))

    if nueva_numero != 0:
        numeros.append(nueva_numero)

"""print("\n*******LISTADO DE NUMEROS*******")
for numero in range(1,len(numeros)):
    print(f" {numero}")"""

numerosiuuu=int(input("Que numero quieres buescar en tu lista?: "))
print("el numero que esco{}giste esta: {} veces.".format((numeros),(numeros.count(numerosiuuu))))


