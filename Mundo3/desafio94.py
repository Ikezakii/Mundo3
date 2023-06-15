dici = {"nome": "", "sexo": "", "idade": 0}
list = []
media = 0
soma = 0
while True:
    dici["nome"] = str(input("Digite o nome da pessoa: ")).capitalize()
    while True:
        dici["sexo"] = str(input("Digite o sexo da pessoa: (M / F) ")).upper()[0]
        if dici["sexo"] in "MF":
            break
        print("Digite M ou F pls")
    dici["idade"] = int(input("Digite a idade: "))
    soma += dici["idade"]
    list.append(dici.copy())

    while True:
        parar = str(input("Deseja continuar? (S / N) ")).upper()[0]
        if parar in "SN":
            break
        print("Apenas S ou N pls")
    if parar == "N":
        break
media = soma / len(list)


print(f"Foram cadastradas {len(list)} pessoas")
print(f"A media de idade delas é {media}")
print(f"As mulheres cadastradas foram ", end = "")
for i in list:
    if i["sexo"] == "F":
        print(i["nome"], end = " ")
print()
print(f"As pessoas com idade acima da média foram ", end = "")
for i in list:
    if i["idade"] >= media:
        print(i["nome"], end = " ")
print()


