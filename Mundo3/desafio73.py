t = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
     'Atlético', 'Atlético-PR', 'Cruzeiro', 'Botafogo', 'Santos',
     'Bahia', 'Fluminense', 'Corinthians', 'Chapecoense', 'Ceará SC',
     'Vasco', 'Sport Recife', 'América-MG', 'Vitória', 'Paraná')


print(f"Os cinco primeiros times -> {t[:5]}")
print(f"Os ultimos 4 colocados -> {t[16:]}") # ou -4
print(f"Times em ordem alfabética ->{sorted(t)}")
print(f"A Chapecoense está na posição {t.index('Chapecoense')+1}")