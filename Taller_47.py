#47. Crear un Programa que permita conocer la mayor estatura dentro un grupo de N estudiantes.  

numerodeestudiantes= int(input("Digte el numero de estudiantes: "))
lista = []
i = 0 
while i < numerodeestudiantes:
    estatura = float(input("Digite la estatura del estudiante: "))
    lista.append(estatura)
    i+= 1
max_altura = max(lista)

print(f"La mayor estatura es de {max_altura:.2f}.")
