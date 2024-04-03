# Programa que permita realizar los siguientes requerimientos: 1. Calcular distancia recorrida 2. 
#Calcular tiempo 3. Calcular velocidad 
#Dependiendo de lo que seleccione el usuario se debe solicitar los datos correspondientes y la 
#operación adecuada, teniendo en cuenta el movimiento rectilíneo uniforme cuya principal ecuación 
#-es: X=V*T. 

print('''
        menu
      1-Calcular la distacia.
      2-Calcular tiempo.
      3-Calcular velociad.''')
num1=int(input("\nUsuario ingresa a una obcion"))
if num1==1:
    print("Calcular la distancia. ")
    def disre(vel, tie):
        dis= vel * tie
        return dis
    vel= float(input("Ingresa la velocidad: "))
    tie = float(input("Ingresa el tiempo: "))
    dis = disre(vel, tie)
    print("La distancia recorrida es:", dis)

if num1==2:
    print("Calcular la tiempo. ")
    vel= float(input("Ingresa la velocidad: "))
    dis = float(input("Ingresa el tiempo: "))
    tie= vel / dis
    print("La distancia recorrida es:", tie)


if num1==3:
    print("Calcular la velocidad. ")
    tie= float(input("Ingresa la tiempo: "))
    dis = float(input("Ingresa el distnancia: "))
    vel= dis/tie
    print("La distancia recorrida es:", vel)

else:
    print("Pana vuelve atras.")
