frase = input("Digite uma frase:\n")

palavras = frase.split()
for i in range(len(palavras)):
    print(*palavras)
    palavras.pop(0)
