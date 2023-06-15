tupla = ("Lapis", 2, "Borracha", 4.50,"Caderno", 14.90, "Mochila", 90)

print("-" * 40)
print(f"{'Listagem de preço':^40}")
print("-" * 40)

for i in range(0,len(tupla)):
    if i % 2 == 0:
        print(f"{tupla[i]:.<30}", end = "")
    else:
        print(f"R${tupla[i]:>7.2f}")
print("-" * 40)