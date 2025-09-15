print("Digite quatro valores inteiros")

l = []
for _ in range(4):
    i = int(input())
    l.append(i)

iven = 0
odd = 0 
for i in l:
    if i % 2 == 0:
        odd += i
    if i % 2 == 1:
        iven += i

print("Soma dos pares =", odd)   
print("Soma dos impares =", iven)   