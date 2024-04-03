#45. Programa  que  permita  calcular  el  factorial  de  un  número.  El  factorial  corresponde  a  la multiplicación de todos los números naturales anteriores incluyendo el número ingresado. 

num1 = int(input("Ingresa un numero: "))

factorial = 1
i = 1

if num1< 0:
    print("El factorial no está definido para numeros negativos.")
elif num1 == 0:
    print("El factorial de 0 es 1.")
else:
    while i <= num1:
        factorial *= i
        i += 1
    print("El factorial de", num1, "es", factorial,".")
