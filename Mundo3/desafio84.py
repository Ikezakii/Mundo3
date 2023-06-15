lista = []
temp = []
cont = 0
pesado = 0
leve = 0


while True:
    temp.append(str(input("Digite o nome da pessoa: ")))
    temp.append(float(input("Digite o peso da pessoa: ")))
    if cont == 0:
        pesado = temp[1]
        leve = temp[1]
    else:
        if temp[1] > pesado:
            pesado = temp[1]
        if temp[1] < leve:
            leve = temp[1]
    lista.append(temp[:])
    temp.clear()
    cont += 1
    continuar = str(input("Deseja continuar (S / N)? ")).upper()
    if continuar == "N":
        break



print(lista)
print(f"Voce cadastrou {cont} pessoas")
print(f"As pessoas mais pesadas são " , end = "")
for i in lista:
    if i[1] == pesado:
        print(f"{i[0]}...", end = "")
print(f"Com o peso de {pesado}")
print(f"As pessoas mais leves são " , end = "")
for i in lista:
    if i[1] == leve:
        print(f"{i[0]}...", end = "")
print(f"Com o peso de {leve}")