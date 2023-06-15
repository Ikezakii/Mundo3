lista = []


while True:
    v = int(input("Digite um valor: "))
    lista.append(v)
    conti = str(input("Deseja continuar (S/ N)? ")).upper()
    if conti == "N":
        break
listarev = sorted(lista, reverse=True)
print(f"Voce digitou {len(lista)} valores")
print(f"Essa é a lista e ordem decrescente -> {listarev}")
if 5 in lista:
    print(f"O valor 5 foi digitado")
else:
    print("O valor 5 não está na lista")
