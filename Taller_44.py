#44. Programa que reciba N calificaciones de una materia, y luego calcule: a) La nota promedio b) La nota mayor c) Si El estudiante pasa o no la materia (Promedio>=40) 

calcule = int(input("Cuantas notas quiere ingresar: "))
i = 0
lista = []

while i<calcule:
    notas = float(input("Digite la nota: "))
    lista.append(notas)
    i += 1
print(lista)

suma = sum(lista)

promedio = suma/calcule

maximanota = max(lista)

print(f"El promedio fue {promedio}.")
print(f"La nota maxima fue {maximanota}.")

if promedio >= 4.0:
    print(f"Pasa la materia con {promedio}.")
else: 
    print(f"No pasas la materia con {promedio}.")
