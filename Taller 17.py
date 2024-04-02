#Entrada de los datos.

print("Bienvenido al taller numero 17.")

#Hacer un codigo que registre codigo del estudian, nombre, materia y tres notas del 1 al 5.

codi=int(input("Digite el codigo del estudiante: "))
nom=input("Escribe el nombre del estudiante: ")
mat=input("Escribe el nombre de la materia: ")

nota1=int(input("Digite la primera nota del estudiante: "))
nota2=int(input("Digite la segunda nota del estudiante: "))
nota3=int(input("Digite la tercera nota del estudiante: "))
notasuma=nota1+nota2+nota3
notafinal=notasuma/3

#Mostrar los datos.

print("CODIGO DEL ESTUDIANTE:",codi)
print("NOMBRE DEL ESTUDAINTE:",nom)
print("LA MATERIA ES:",mat)
print("LA NOTA FINAL DEL ESTUDIANTE ES:",notafinal)

#Codigo de aprovado a no aprovado.
if notafinal>=4:
    print("El estudiante a aprovado con una nota mayor o igual a 4.0:")
else:
    print("El estudiante a reprobado con una nota menor a 4.0:")
