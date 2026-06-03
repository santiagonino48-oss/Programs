import numpy as np

rng=np.random.default_rng()
num=rng.integers(1,100)
print(num)

i=False

while (i==False):
    intento=int(input("Ingrese un numero: "))
    if intento==num:
        print("Felicidades, acertaste")
        i=True
    elif intento<num:
        print("El numero es mayor")
    elif intento>num:
        print("El numero es menor")
    else:
        print("No es un numero")
