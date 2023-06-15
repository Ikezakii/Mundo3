time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador["nome"] = str(input("Digite o nome do jogador: ")).capitalize()
    tot = int(input(f"Quantas partidas o {jogador['nome']} jogou? "))
    partidas.clear()
    for i in range(tot):
        partidas.append(int(input(f"Quantos gols na partida {i+1}? ")))
    jogador["gols"] = partidas[:]
    jogador["total"] = sum(partidas)
    time.append(jogador.copy())
    while True:
        parar = str(input("Deseja continuar? (S / N) ")).upper()[0]
        if parar in "SN":
            break
        print("Responda com S ou N pls")
    if parar == "N":
        break

print("-" * 30)
print("No. ",end = "")
for i in jogador.keys():
    print(f"{i:<15}", end = "")
print()
print("-" * 30)
for i,j in enumerate(time):
    print(f"{i:>3} ",end = "")
    for d in j.values():
        print(f"{str(d):<15}",end = "")
    print()
print("-" * 30)

while True:
    busca = int(input("Qual jogador deseja ver: "))
    if busca == 999:
        break
    if busca >= len(time):
        print("Não existe")
    else:
        print(f"Dados do jogador {time[busca]['nome']}")
        for i,g in enumerate(time[busca]["gols"]):
            print(f"No jogo {i+1} fez {g}")
    print("-" * 30)