#32. Programa que permita determinar cuántos hombres y mujeres hay en un curso de 25 
#estudiantes. 

generos = []
contadorM=0
contadorF=0
genero = str

for i in range(1,4):
    genero = input("Ingrese un genero: ")

    if genero == 'm':
        generos.append(genero)
    elif genero == 'f':
        generos.append(genero)

for e in generos:
    if e == 'm':
        contadorM=contadorM+1
    elif e == 'f':
        contadorF=contadorF+1
                        
print("Hay tantos hombres: ",contadorM)
print("Hay tantas mujeres: ",contadorF)
