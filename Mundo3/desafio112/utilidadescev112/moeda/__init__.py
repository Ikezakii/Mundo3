def aumentar(n= 0,a=0,show = False):
    d = n * (a/100)
    n = d + n
    if show:
        n = form(n)
    return n # return n if show is False else form(n)


def dobro(n= 0,show = False):
    n = n * 2
    if show:
        n = form(n)
    return n # return n if show is False else form(n)


def diminuir(n= 0,d=0,show = False):
    d = n * (d / 100)
    n = n - d
    if show:
        n = form(n)
    return n # return n if show is False else form(n)


def metade(n= 0,show = False):
    n = n/2
    if show:
        n = form(n)
    return n # return n if show is False else form(n)


def form(n = 0, m = "R$"):
    return f"{m}{n:.2f}".replace(".",",")




def resumo(n, a, d):
    print("-" * 19)
    print("  Resumo de Valor")
    print("-" * 19)
    print(f"Preço analisado -> {form(n)}")
    print(f"Dobro do preço -> {dobro(n,True)}")
    print(f"Metade do preço ->{metade(n,True)}")
    print(f"{a}% aumentado -> {aumentar(n,a,True)}")
    print(f"{d}% de redução -> {diminuir(n,d,True)}")


