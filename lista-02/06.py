numeros = []

for i in range(1, 11):
    if i % 2 == 0:
        numeros.append(-i)
    else:
        numeros.append(i)

print("Resultados:", *numeros)