n1 = int(input("Digite um valor: "))
n2 = int(input("Digite um valor: "))
n3 = int(input("Digite um valor: "))
n4 = int(input("Digite um valor: "))

tupla = (n1,n2,n3,n4)

print(f"O valor 9 apareceu {tupla.count(9)} vezes")
if 3 in tupla:
    print(f"O 3 apareceu pela primeira vez na posição {tupla.index(3)+1}") # +1? sla pode ser fica mais facil pra conferir
else:
    print("O valor 3 não está na tupla")

print(f"Os numeros pares foram ", end= '')
for n in tupla:
    if n % 2 == 0:
        print(n, end = " ")

