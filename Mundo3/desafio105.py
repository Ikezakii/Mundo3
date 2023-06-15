def notas(*n, sit = False):

    dici = {}
    dici["total"] = len(n)
    dici["maior"] = max(n)
    dici["menor"] = min(n)
    media = sum(n) / len(n)
    dici["media"] = media
    if sit:
        if media >= 7:
            dici["situação"] = "BOA"
        elif media >= 5:
            dici["situação"] = "RAZOAVEL"
        else:
            dici["situação"] = "RUIM"
    return dici



n = notas(5,8,7,8, sit=True)
print(n)