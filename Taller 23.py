#Hacer un programa para determinar si un deportista es aceptado en el equipo de baloncesto de Bogotá.

print("Bienvenido al taller numero 23.")

#Edad.
edad=int(input("Digite la edad del aspirante: "))

#Estatura
estatura=float(input("Digite la estatura del aspirante: "))

#Peso
peso=int(input("Digite el peso del aspirante: "))

#La edad debe ser menor o igual a 18 años, la estatura debe ser igual o mayor a 180cm y el peso debe ser igual o menor a 80kg.
if edad<=18:
    print("El aspirante aprueba el requerimiento con",edad,"años.")
else:
    print("El aspirante no aprueba el requerimiento con",edad,"años.")
if estatura>=180:
    print("El aspirante aprueba el requerimiento con",estatura,"cm.")
else:
    print("El aspirante no aprueba el requerimiento con",estatura,"cm.")
if peso<=80:
    print("El apirante aprueba el requerimiento con",peso,"kg.")
else:
    print("El aspirante no aprueba el requerimiento con",peso,"kg.")

#El aspirante debe aprobar con los 3 requerimientos.
if edad<=18 and estatura>=180 and peso<=80:
    print("El apirante a subido de rango a estudiante.")
else:
    print("El aspirante sigue siendo aspirante.")
