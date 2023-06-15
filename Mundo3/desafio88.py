from random import randint
from time import  sleep
lista = []
temp = []
total = 1
vezes = int(input("Quantos jogos deseja fazer? "))
while total <= vezes:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in temp:
            temp.append(num)
            cont += 1
        if cont >= 6:
            break
    temp.sort()
    lista.append(temp[:])
    temp.clear()
    total += 1


for i , l in enumerate(lista):
    print(f"Jogo {i+1}: {l}")
    sleep(1)