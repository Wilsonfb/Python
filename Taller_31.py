#31. Programa que permita determinar cuántos estudiantes son mayores de edad en un grupo de 20 
#estudiantes.

edades = []
contador=0
edad = int

for i in range(1,5):
    edad = int(input("Ingrese una edad: "))

    if edad >= 1:
        edades.append(edad)
        print("Aqui voy 1")

for e in edades:
    if e >= 18:
        contador=contador+1
        print("Aqui voy 2")
            
            
print("Mayores de edad: ",contador)

"""
for pelicula in peliculas: # Mientras quede en el elementos de pelicula ve iterDO y ve guardando cada uno de los elemento en pelicula.
    print(f"{peliculas.index(pelicula)+1}. {pelicula}") """