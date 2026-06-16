def es_palindromo(palabra):
    return palabra==palabra[::-1]

palabra=input("Ingresa tu palabra")
if es_palindromo(palabra):
    print(f"\n{palabra} es un palindromo\n")
else:
 print (f"\n{palabra} no es palindromo\n")