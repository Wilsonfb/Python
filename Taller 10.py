##Programa para saber el salario que se le debe pagar a un trabajador.

print("Bienvenido al taller 10.")

#Salario diario.
print("Digite a cuanto esta el dia del salario:")
diario=float(input())

#Numero de dias trabajados.
print("Digite el numero de dias que trabajo el empleado:")
dias=int(input())
sueldo=diario*dias
suelfin=sueldo*.25
sueldoto=sueldo-suelfin

print("Este es el salario final que le debe pagar al trabajador",sueldoto)
