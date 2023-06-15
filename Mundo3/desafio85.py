lista = [[],[]]

for i in range (7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        lista[0].append(num)
    elif num % 2 != 0:
        lista[1].append(num)

print(f"A lista completa {lista}")
print(f"a lista dos numeros pares {sorted(lista[0])}")
print(f"A lista dos numeros impares {sorted(lista[1])}")
