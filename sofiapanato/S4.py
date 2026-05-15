a=float(input("ingrese sueldo: "))

if a<8000 :
    b=a*0.12
    print (f"\nTu sueldo es: {a} \nTu bonificacion es: {b} \nTu sueldo total es de: {a+b}")
else:
     b=a*0.08
     print (f"\nTu sueldo es: {a} \nTu bonificacion es: {b}\nTu sueldo total es: {a+b}")