dici = {"jogador": "", "gols": [], "total": 0}
total = 0

dici["jogador"] = str(input("Nome do jogador: ")).capitalize()
jogos = int(input(f"Quantos jogos {dici['jogador']} jogou? "))

for i in range(jogos):
    dici["gols"].append(int(input(f"Quantos gols na partida {i+1}? ")))


for gol in dici["gols"]:
    total += gol

dici["total"] = total
print("-=" * 30)
for k, v in dici.items():
    print(f"O campo {k} tem valor {v}")


print("-=" * 30)
print(f"{dici['jogador']} jogou {jogos} partidas")
for i in range(jogos):
    print(f"Na partida {i+1}, fez {dici['gols'][i]}")
print(f"Total de gols: {dici['total']}")