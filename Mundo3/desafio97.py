def texto(txt):
    print("-" * (len(txt)+4))
    print(f"  {txt}")
    print("-" * (len(txt)+4))

pala = str(input("Digite algo: "))
texto(pala)