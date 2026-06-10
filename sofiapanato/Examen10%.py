ventas=[
    [5,3,4,6,2,1,7],
    [8,6,7,5,4,3,2],
    [2,3,1,4,5,6,2]
]

print("")
Pmax=float('-inf')
for i, semana in enumerate(ventas):
    total= sum(semana)
    if total<= 25:
        print(f"La demanda de la semana {i+1} fue BAJA con {total} ventas \n")
    elif total >=26:
        print(f"La demanda de la semana {i+1} fue ALTA con {total} ventas \n")
    
    if Pmax<total:
        Pmax=total
        Pmaxi=i+1

print(f"El producto mas vendido fue el de la semana {Pmaxi} con {Pmax} ventas \n")