def leaidin(msg):
    ok = False
    while not ok:
        ent = str(input(msg)).replace(",",".").strip()
        if ent.isalpha() or ent == "":
            print("Preço inválido")
        else:
            ok = True
            return float(ent)