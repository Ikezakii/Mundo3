def voto(ano):
    from datetime import date #declarar dentro da função para economizar memoria
    atual = date.today().year
    idade = atual - ano
    if idade == 17 or idade == 16 or idade >= 65:
        print(f"Com {idade} anos: VOTO OPCIONAL")
    elif idade >= 18:
        print(f"Com {idade} anos: VOTO OBRIGATÓRIO")
    else:
        print(f"Com {idade} anos: NÃO PRECISA VOTAR")


nasc = int(input("Que ano voce nasceu? "))
voto(nasc)