L0=[10,2.0,True,30,40,['a','b','c']]
L1=[L0[0]]
L1.extend(L0[3:5])
print("L1:", L1)

L2=[] + L1

L2.append(L0[5])

print("L2:", L2)

L2.extend(L0[5])
print("L2:", L2)
L2=L2 + ['D','E','F']
print("L2:", L2)


L3=[10, 30, 40, ['a', 'b', 'c']]
print("rango sublista", L3[3][1:3])



L3=[i for i in range(10)]

print("L3:", L3)


L4= sorted(L3, reverse = True) #da la vuelta a la lista modificándola

print ("L3", L3) #sorted ordena la lista sin modificarla (ordena una nueva)
print ("L4:", L4)
L5=sorted(L4)
print("L5", L5)

L4.sort() #sort ordena la lista modificándola

L6=L4.sort()
print("L4:", L4)
print("L6:", L6)


L6=list(reversed(L4))

print("L6:", L6)

print("L6:", L6[:-1])
print("L6:", L6[-1::-1])


dicc = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u', ' ':''}
print("claves: ",dicc.keys())
print("valores: ",dicc.values())

print(dicc.get('á'))

for k, v in dicc.items():
    if v=='i':
        print("clave", k)

print(dicc ['í'])

def esPalindromo(cadena):
    cadSinEspacios= cad.replace(' ','')
    cadSinTildes=''
    for c in cadSinEspacios:
        cadSinTildes += dicc.get(c, c)

    return cadSinTildes == cadSinTildes[::-1]



cad='ánita lava la tina'



print(f"es palíndromo {cad}:", {esPalindromo(cad)})