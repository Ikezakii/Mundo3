lista = []

for c in range(5):
    v = int(input("Digite um valor: "))
    if c == 0 or v > lista[-1]:
        lista.append(v)
        print("Valor adicionado na ultima posição")
    else:
        cont = 0
        while cont < len(lista):
            if v <= lista[cont]:
                lista.insert(cont, v)
                print(f"Adicionado na posição {cont}")
                break
            cont += 1
print(lista)

