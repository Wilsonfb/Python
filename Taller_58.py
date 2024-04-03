#58. Programa que permita llenar dos vectores de 12 posiciones y luego en un tercer y cuarto vector 
#guardar la suma y resta de cada posición. Al final se deben mostrar de forma completa todas las 
#sumas y restas realizadas. 

lista1 = []
lista2 = []

for i in range(12):
    num1 = int(input("Digite un numero para la primera lista: "))
    num2 = int(input("Digite un numero para la segunda lista: "))
    lista1.append(num1)
    lista2.append(num2)

suma_lista = [num1+num2 for num1, num2 in zip(lista1, lista2)]
resta_lista = [num1-num2 for num1, num2 in zip(lista1, lista2)]

print("Suma de listas por posicion.")
for i, suma in enumerate(suma_lista):
    print(f"Posición {i+1}: {suma}.")

print("Resta de listas por posicion.")
for i, resta in enumerate(resta_lista):
    print(f"Posición {i+1}: {resta}.")
