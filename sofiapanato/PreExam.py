import numpy as np

matriz = np.random.randint(50, 150, size=(5, 5))

for fila in matriz:
    print(fila) 

matrizM = np.zeros((5, 5))


for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] <= 70:
            matrizM[i][j] = 1
            
        elif matriz[i][j] > 70 and matriz[i][j]:
            matrizM[i][j] = 0

print ("\nCordenadas de los defectuosos\n")
for fila in matrizM:
    print(f"{fila}")

total= np.sum(matriz)/(5*5)
if total <= 90:
    print("\nEl lote es defectuoso")
    print(f"\nEl promedio de la matriz es: {total}")
else:
    print("\nEl lote es aceptable")
    print(f"\nEl promedio de la matriz es: {total}")




