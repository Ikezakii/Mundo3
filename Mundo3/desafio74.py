from random import randint

list = []

for i in range(5):
    num = randint(1,10)
    list.append(num)

tu = sorted(list)
# é possivel fazer tupla = (radint(1,10), radint(1,10), e por ai vai)

print(f"Aqui estão os numeros gerados: " , end='')
for n in tu:
    print(f"{n}", end=' ')
print(f"\nO menor valor é {min(tu)} e o maior é {max(tu)}")
