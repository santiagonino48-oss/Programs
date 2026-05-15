a=int(input("ingrese el rango de numeros: "))

sPares=0
sImpares=0
cImprares=0

for i in range(1,a+1):
    if i%2==0:
        sPares=sPares+i
    else:
        sImpares=sImpares+i
        cImprares=cImprares+1
        
print("la suma de los pares es: ",sPares)

if cImprares>0:
    promedio=sImpares/cImprares
    print("el promedio de los impares es: ",promedio)
else:
    print("no hay impares")