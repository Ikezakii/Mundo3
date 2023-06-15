lista = []
listp = []
listi = []

while True:
    v = int(input("Digite um valor: "))
    lista.append(v)

    conti = str(input("Deseja continuar (S/ N)? ")).upper()
    if conti == "N":
        break
for i in lista:
    if i % 2 == 0:
        listp.append(i)
    elif i % 2 != 0:
        listi.append(i)

print(lista)
print(listp)
print(listi)

