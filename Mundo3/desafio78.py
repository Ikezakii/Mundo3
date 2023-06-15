lista = []

for i in range (5):
    v = int(input(f"Digite um valor para posição {i}: "))
    lista.append(v)
    vmax = max(lista)
    vmin = min(lista)

print(f"Voce digitou os valores {lista}")
print(f"O maior valor digitado foi {max(lista)} na posição ", end = "")
for i, v in enumerate(lista):
    if v == vmax:
        print(f"{i}...", end = "")
print()
print(f"O menor valor digitado foi {min(lista)} na posição ", end = "")
for i, v in enumerate(lista):
    if v == vmin:
        print(f"{i}...", end = "")
