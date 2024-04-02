#Hacer un codigo que permita ingresar los valores de temperatura de cada día durante una semana.

print("Bienvenido al taller numero 21.")

dia1=int(input("Digita la temperatura del Lunes: "))
dia2=int(input("Digita la temperatura del Martes: "))
dia3=int(input("Digite la temperatura del Miercoles: "))
dia4=int(input("Digite la temperatura del dia Jueves: "))
dia5=int(input("Digite la temperatura del Viernes: "))
dia6=int(input("Digite la temperatura del Sabado: "))
dia7=int(input("Digite la temperatura del Domingo: "))

tem=dia1+dia2+dia3+dia4+dia5+dia6+dia7
promediodetem=tem/7

print("La temperatura promedio de toda la semna es",promediodetem,"grados")

#Hacer un codigo que si el promedio es mayor a 35° mostrar el mensaje “Que semana tan calurosa”.
if promediodetem>35:
    print("Que semana tan calurosa.")
#Si el promedio es menor de 15° mostrar el mensaje “Que semana tan fría”
elif promediodetem<15:
    print("Que semana tan fria.")
# Si el promedio esta entre 15° y 35° mostrar el mensaje “Que clima tan delicioso” 
else:
    print("Que clima tan delicioso.")
    