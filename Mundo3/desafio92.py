from datetime import datetime

dici = {"nome": "", "idade": 0, "ctps": 0}


dici["nome"] = str(input("Nome: ")).capitalize()
ano = int(input("Ano de nascimento: "))
dici["idade"] = 2023 - ano
dici["ctps"] = int(input("Carteira de trabalho (0 se não tem uma): "))
if dici["ctps"] == 0:
    for k,v in dici.items():
        print(f"{k} tem valor {v}")
else:
    dici["contratação"] = int(input("Ano de cnotratação: "))
    dici["salario"] = float(input("Salário: R$"))
    dici["aposentadoria"] = dici["idade"] + ((dici["contratação"] + 35) - datetime.now().year)
    for k,v in dici.items():
        print(f"{k} tem valor {v}")