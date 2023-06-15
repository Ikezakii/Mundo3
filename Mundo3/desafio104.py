def leiaint(msg):
    ok = False
    v = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            v = int(n)
            ok = True
        else:
            print("\033[0;31mDigite um valor INTEIRO válido\033[m")
        if ok:
            break
    return v


n = leiaint("Digite um numero inteiro: ")
print(f"Voce digitou {n}")