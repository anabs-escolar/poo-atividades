print("Informe o número do mês")
i = int(input())

meses = [
    "janeiro",
    "fevereiro",
    "março",
    "abril",
    "maio",
    "junho",
    "julho",
    "agosto",
    "setembro",
    "outubro",
    "novembro",
    "dezembro"
]

print("")

if i >= 1 and  i <= 3:
    print(f"O mês {meses[i-1]} é do primeiro trimestre do ano")
    
elif i >= 4 and  i <= 5:
    print(f"O mês {meses[i-1]} é do segundo trimestre do ano")    

elif i >= 7 and  i <= 9:
    print(f"O mês {meses[i-1]} é do terceiro trimestre do ano")

elif i >= 10 and  i <= 12:
    print(f"O mês {meses[i-1]} é do quarto trimestre do ano")
