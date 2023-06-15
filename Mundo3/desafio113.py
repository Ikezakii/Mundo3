def leiaint(msg):
    ok = False
    v = 0
    while True:
        try:
            n = int(input(msg))

        except Exception as erro:
                print(f"\033[0;31mAlg deu errado -> {erro}\033[m")
                continue
        except(KeyboardInterrupt):
            print("\n\033[0;31mUsuário interrompeu o sistema\033[m")
            return 0
        else:
            ok = True
            v = n
        if ok:
            break
    return v


def leiafloat(msg):
    ok = False
    v = 0
    while True:
        try:
            n = float(input(msg))

        except(ValueError,TypeError):
                print(f"\033[0;31mDigite um Numero real valido\033[m")
                continue
        except(KeyboardInterrupt):
            print("\n\033[0;31mUsuário interrompeu o sistema\033[m")
            return 0
        else:
            ok = True
            v = n
        if ok:
            break
    return v


n = leiaint("Digite um numero inteiro: ")
f = leiafloat("Digite um numero inteiro: ")
print(f"Voce digitou {n} e {f}")