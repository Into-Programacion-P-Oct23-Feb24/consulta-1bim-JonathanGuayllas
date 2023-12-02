par = int(input("Ingrese un numero par mayor a 0 y positivo: "))

if (par > 0) and (par % 2 != 1):
    print("El numero ingresado es: {}".format(par))
else:
    print("El número ingresado no es par")
