from random import randint
from time import sleep
from operator import itemgetter
rank = {}
jogadores = {"jogador1": randint(1,10),
             "jogador2": randint(1,10),
             "jogador3": randint(1,10),
             "jogador4": randint(1,10)}
print("VALORES SORTEADOS")
for k, v in jogadores.items():
    print(f"{k} tirou {v}")
    sleep(1)

rank = sorted(jogadores.items(), key = itemgetter(1), reverse = True)
print("RANKING DOS JOGADORES")
for k, v in enumerate(rank):
    print(f"{v[0]} com {v[1]}")






