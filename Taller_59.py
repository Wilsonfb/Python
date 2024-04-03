#59. Programa que permita llenar un vector de N posiciones y luego en un segundo y tercer vector 
#guarde el cuadrado y el cubo de cada una de las posiciones. Finalmente imprimir el contenido de 
#todos los vectores

lista = []
cuadrado = []
cubo = []

pos = int(input("Cuantas posiciones quiere en la lista: "))

for i in range(pos):
    num = int(input("Digite un numero para la lista: "))
    lista.append(num)

cuadrado_lista = [num ** 2 for num in lista]
cubo_lista = [num ** 3 for num in lista]

cuadrado.append(cuadrado_lista)
cubo.append(cubo_lista)

print(f"Los numeros de la lista la cuadrado son: \n{cuadrado}.")
print(f"Los numeros de la lista al cubo son: \n{cubo}.")
