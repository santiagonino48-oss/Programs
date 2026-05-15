a=int(input("ingrese la calificacion: "))

if a>=0 and a<=5:
    print(f"\nReprobado con: {a}\n")
elif a>=6 and a<=10:
    print(f"\nAprobado con: {a}\n")
else:
    print("\nCalificacion no valida\n")