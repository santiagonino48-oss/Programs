import numpy as np

rng=np.random.default_rng()

matriz = [
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]  
for i in range (0,5):
        for j in range (0,5):
         if (matriz[i][j])== 0:
            x=int(rng.integers(1,9))
            matriz[i][j]=x
   

for fila in matriz:
   print (fila)




