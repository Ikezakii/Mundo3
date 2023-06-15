from random import randint

lista = []

def sorteio(lista):
    for i in range(5):
        lista.append(randint(1,10))
    print(f"Os valores da lista -> ", end = " ")
    for v in lista:
        print(v, end = " ")
    print()
    print(f"A soma dos numeros pares da lista -> {somapar(lista)}")


def somapar(lista):
    soma = 0
    for v in lista:
        if v % 2 == 0:
            soma += v
    return soma



sorteio(lista)