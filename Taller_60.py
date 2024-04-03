#60. Programa que permita Ingresar el número de estudiantes asignados cada uno de los 20 salones 
#de un colegio y luego satisfacer los siguientes requerimientos: a) Determinar la cantidad total de 
#estudiantes b) Determinar el curso con mayor cantidad de estudiantes c) Determinar el curso con 
#menor cantidad de estudiantes 

curso = []

for i in range(20):
    estu = int(input(f"Cuantos estudiante hay en el salon {i+1}: "))
    curso.append(estu)

total_estu = sum(curso)

for i in curso:
    mas_estu = max(curso)
    i_max = curso.index(mas_estu)
    min_estu = min(curso)
    i_min = curso.index(min_estu)

print(f"La suma de todos los salones es {total_estu}.")
print(f"El salon con mas estudiantes es {i_max+1} con {mas_estu} estudiantes.")
print(f"El salon con menos estudiantes es {i_min+1} con {min_estu} estudiantes.")
