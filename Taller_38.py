#38. Programa que permita determinar si un estudiante que recibe 15 notas gana o no la materia de Programación De Software. Se gana la materia si el promedio es mayor o igual a 4.0.

notas = []

for i in range(1,16):
    nota = float(input(f"Digite la nota {i}: "))
    notas.append(nota)
print(notas)

suma = sum(notas)
promedio = suma/15

if promedio >= 4.0:
    print(f"Pasaste la materia con una nota de {promedio}.")
else:
    print(f"No pasaste la materia por tener {promedio}.")
