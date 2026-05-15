num = int(input("ingrese un numero entero"))
if (num>=0) and (num<=9):
   print ("el numero ingresado es una unidad")
elif (num>=10) and (num<=99):
    print ("el numero ingresado es una decena")
else: 
    print("el numero ingresado es una centena u otro")