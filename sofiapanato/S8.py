a=int(input("ingrese el rango de numeros: "))
serie= 0

for i in range(1,a+1):
    serie += i**i
print("la suma de los numeros al cuadrado es: ",serie)