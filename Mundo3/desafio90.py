dici = {"nome": "", "nota": 0, "situação": ""}

dici["nome"] = str(input("Digite o nome do aluno: ")).capitalize()
dici["nota"] = float(input("Digite a média do aluno: "))

if dici["nota"] > 7:
    dici["situação"] = "Aprovado"
else:
    dici["situação"] = "Reprovado"

for k, v in dici.items():
    print(f"{k} = {v}")
