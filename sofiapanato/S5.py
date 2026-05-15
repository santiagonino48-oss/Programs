a = float(input("ingrese el sueldo: "))
b = int(input("ingrese el nivel: "))

if b == 1 :
    c=a*0.12
    print (f"\nEl nivel del empleado es: {b}\nTu sueldo es: {a} \nTu bonificacion es: {c} \nTu sueldo total es de: {a+c}")

elif b == 2: 
    c=a*0.08
    print (f"\nEl nivel del empleado es: {b}\nTu sueldo es: {a} \nTu bonificacion es: {c} \nTu sueldo total es de: {a+c}")

elif b == 3 :
    c=a*0.05
    print (f"\nEl nivel del empleado es: {b}\nTu sueldo es: {a} \nTu bonificacion es: {c} \nTu sueldo total es de: {a+c}")
 
elif b == 4:
    c=a*0.038
    print (f"\nEl nivel del empleado es: {b}\nTu sueldo es: {a} \nTu bonificacion es: {c} \nTu sueldo total es de: {a+c}")
 
else:
    print(f"no existe el nivel el sueldo se mantiene igual: {a}")
    
#fin