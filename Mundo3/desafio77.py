tupla = ('Sour','Brutal','Traitor','Drivers License','1 step foward, 3 steps back','deja vu','good 4 u')

for i in tupla:
    print(f"\nNa palavra {i.upper()} temos ", end = "")
    for letra in i:
        if letra.lower() in "aeiou":
            print(letra, end = " ")

