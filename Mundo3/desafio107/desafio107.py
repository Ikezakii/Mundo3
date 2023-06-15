import uteis

m = float(input("Digite o valor: R$"))
print(f"A metade de {uteis.form(m)} é {uteis.metade(m,True)}")
print(f"O dobro de {uteis.form(m)} é {uteis.dobro(m,True)}")
print(f"Aumentando em 10% fica {uteis.aumentar(m,True)}")
print(f"Diminuindo em 13% fica {uteis.diminuir(m,True)}")