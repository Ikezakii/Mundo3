def ficha(nome = "", gols = 0):
    if nome == "":
        nome = "<desconhecido>"
    print(f"O jogador {nome} fez {gols} gols no campeonato")


n = str(input("Digite o nome do jogador: ")).capitalize().strip()
g = str(input("Quantos gols ele fez? "))
if g.isnumeric():
    g = int(g)
else:
    g = 0
ficha(n, g)