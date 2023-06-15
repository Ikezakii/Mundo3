def pyhelp(msg):
    help(msg)


comando = ""
while True:
    comando = str(input("Função ou Biblioteca: "))

    if comando.upper() == "FIM":
        break
    else:
        pyhelp(comando)