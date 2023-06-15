def area(b, h):
    a = b * h
    print("-" * 30)
    print(f"Largura = {b}")
    print(f"Comprimento = {h}")
    print(f"A área do terreno é {a}")


l = float(input("Digite a largura: "))
c = float(input("Digite o comprimento: "))

area(l,c)