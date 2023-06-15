from time import sleep

def cont(a, b, c):
    if c < 0:
        c *= -1
    if b > a:
        if c == 0:
            c = 1
        numeros = list(range(a ,b+1,c))
        for n in numeros:
            print(f"{n}",end = " ")
        print()
    elif b < a :
        if c < 0:
            if c == 0:
                c = 1
            rever = list(range(a, b - 1, c))
        else:
            if c == 0:
                c = 1
            rever = list(range(a, b-1,-c))
        for n in rever:
            print(f"{n}",end = " ")
        print()



print("-*" * 30)
cont(0,10,1)
print("-*" * 30)
cont(10,0,2)
print("-*" * 30)
print("Agora é sua vez")
inicio = int(input("Digite o inicio: "))
fim = int(input("Digite o fim da sequencia: "))
passo = int(input("Digite quantos passos a sequencia deve dar: "))
cont(inicio,fim,passo)



