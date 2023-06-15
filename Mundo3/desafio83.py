ex = str(input("Digite a expressão: "))
exp = []

for i in ex:
    if i == "(":
        exp.append("(")
    elif i == ")":
        if len(exp) > 0:
            exp.pop()
        else:
            exp.append(")")
            break

if len(exp) == 0:
    print("A expressão está correta")
else:
    print("A expressão está errada")