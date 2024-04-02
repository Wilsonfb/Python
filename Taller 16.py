#Hacer un programa en el cual se ingresen 2 números.

print("Bienvenido al taller numero 16.")

num1=int(input("Digite el primer numero:"))
num2=int(input("Digite el segundo numero:"))

resta=num1-num2
suma=num1+num2

#Hacer un codigo que si los números son iguales restarlos.

if num1==num2:
    print("Los numeros que digitaste son iguales y la resta de estos es:",resta)
    
#Hacer un codigo que si los numeros son diferentes sumarlos.
    
elif num1!=num2:
    print("Los numeros que digitaste son diferentes la suma de estos es:",suma)
    