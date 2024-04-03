#34.  Programa que permita calcular la estatura promedio de un grupo de 18 estudiantes y luego tomar las siguientes decisiones: a) Si la estatura promedio es menor a 140 cm imprimir un mensaje que diga “Estudiantes muy bajos”. b) Si la estatura promedio se encuentra entre 140 y 170 cm imprimir “Estudiantes de estatura normal”. c) Si la estatura promedio es mayor de 170 cm imprimir “Estudiantes muy altos”. 

lista = []

for i in range(0,18):
    estatura = int(input("Cual es la estatura: "))
    lista.append(estatura)
print(lista)

suma = sum(lista)
promedio = suma/18

if promedio < 140:
    print("Estudiantes muy bajos.")
elif promedio >= 140 and promedio<= 170:
    print("Estudiantes de estatura normal.")
elif promedio > 170:
    print("Estudiantes muy altos.")
