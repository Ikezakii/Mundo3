temp = []
lista = []
media = 0

while True:
    nome = (str(input("Digite o nome do aluno: "))).capitalize()
    temp.append(nome)
    temp.append(float(input("Nota 1: ")))
    temp.append(float(input("Nota 2: ")))
    lista.append(temp[:])
    temp.clear()

    resu = str(input("Deseja continuar (S / N)? ")).upper()
    if resu  == "N":
        break

for i , l in enumerate(lista):
    media = (l[1] + l[2])/ 2
    print(f"{i} - {l[0]} - media: {media}")
while True:
    esc = int(input("Deseja ver a nota de qual aluno (para interromper digite 999)? "))
    if esc == 999:
        break
    if esc <= len(lista) - 1:
        print(f"Notas do(a) Aluno(a) {lista[esc][0]} -> {lista[esc][1]}, {lista[esc][2]}")

