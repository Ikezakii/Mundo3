def maior(*num):
    cont = 0
    maior = 0
    print("-*" * 30)
    for v in num:
        print(v,end = " ")
        if cont == 0:
            maior = v
        else:
            if v > maior:
                maior = v
        cont += 1
    print(f" ||| Foram informados {len(num)} numeros")
    #print()
    print(f"O maior valor foi {maior}")




maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

