lista = [[0,0,0],[0,0,0],[0,0,0]]
#listapar = []
somater = 0
somap = 0

for l in range (3):
    for c in range (3):
        lista[l][c] = int(input(f"Digite um valor para [{l}][{c}]: "))
        #if lista[l][c] % 2 == 0:
            #listapar.append(lista[l][c])

for l in range (3):
    for c in range (3):
        print(f"[{lista[l][c]:^5}]", end = "")
        if lista[l][c] % 2 == 0:
            somap += lista[l][c]
    print()

#for i in listapar:
    #somap += i

for i in lista:
    somater += i[2]

print(f"A soma dos valores pars é {somap}")
print(f"O maior valor da segunda linha é {max(lista[1])}")
print(f"A soma dos valores da terceira coluna é {somater}")



