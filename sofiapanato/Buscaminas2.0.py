import numpy as np
nombre=(input("\nDime tu nombre:"))

nivel=int(input("\nQue dificultad quieres Facil(1) Normal(1) Dificil(3)"))
contador=int(0)

print("")

def tablero ():
    tablero= np.random.randint(0,2 , size=(4, 4))
    return tablero

def tablero_memoria ():
    tablero_memoria= np.zeros((4,4))
    return tablero_memoria

def validar_jugadas(posx,posy,tablero,tablero_memoria):
    if tablero_memoria[posx][posy]!=0:
        return "Movimiento repetido"
    else:
        if tablero[posx][posy] == 1:
            tablero_memoria[posx][posy]=1
            return "Impacto"
        else:tablero_memoria[posx][posy]=0
        return "Sin Impacto"


if 1== nivel:
  print("nivel facil")
  jugadas = 3
elif 2 == nivel:
    print("nivel medio")
    jugadas = 6
elif 3 == nivel:
    print("nivel dificil")
    jugadas = 9
else:
    print("nivel invalido, se asignara nivel facil")
    jugadas = 3

tablero_real = tablero()
memoria_real = tablero_memoria()

for k in range (0,jugadas)  :

    posx=int(input("\nIngresa tu cordenada X "))
    posy=int(input("\nIngresa tu cordenada Y "))

    texto=validar_jugadas(posx,posy, tablero_real , memoria_real )
    if texto=="Movimiento repetido":
        print(f"La jugada ya fue realizada")
    elif texto=="Impacto":
        contador+=1
        print("Acertaste a una mina, se te suma un punto ")
    elif texto =="Sin Impacto":
        print("Fallaste pa lo siento")
    


print("\nEl tablero real era:")
print (tablero_real)