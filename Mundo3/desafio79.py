lista = []


while True:
    v = int(input("Digite um valor: "))
    if v in lista:
        print("Valor duplicado, nao irei adicionar")
    else:
        lista.append(v)

    conti = str(input("Deseja continuar (S/ N)? ")).upper()
    if conti == "N":
        break

print(lista)
