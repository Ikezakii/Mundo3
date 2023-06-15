nums = ("Zero","Um","Dois","Tres","Quatro","Cinco","Seis","Sete","Oito","Nove"
        ,"Dez","Onze","Doze","Treze","Quatorze","Quinze","Dezesseis","Dezessete","Dezoito","Dezenove","Vinte")

while True:
    esc = int(input("Digite um numero entre 0 a 20: "))
    if esc >= 0 and esc <= 20:
        break
    else:
        print("Digite um numero válido")

print(nums[esc])