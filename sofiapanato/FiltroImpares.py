def filtar_pares (lista):
    return[ for n in lista if n % 2 == 0]
lista=[0,5,8,3,4,8,6,9,11,12]

pares= filtar_pares(lista)

print(pares)