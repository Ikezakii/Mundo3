def fatorial(num, show = False):
    """-> Calcula o fatorial de um numero.
    Primeiro parametro recebe o numero a ser calculado.
    Segundo parametro (opcional) serve para mostra ou nao as contas.
    Função possui um retrono de valor."""
    fat = num - 1
    if num == 0:
        num = 1
    else:
        while fat != 0:
            if show:
                print(f"{num} x {fat} = {num*fat}")
            num *= fat
            fat -= 1
    return num







print(fatorial(0,show=True))