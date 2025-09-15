
def diff(nums: list[int]) -> bool:
    count = 0
    for n in l:
        for m in l:
            if m == n:
                count+=1
            if count > 1:
                return False
        count = 0
    return True 

print("Digite quatro valores inteiros")

l = []
for _ in range(4):
    i = int(input())    
    l.append(i)

if diff(l):
    print("Maior valor =", max(l))
    l.remove(max(l))
    
    print("Menor valor =", min(l))
    l.remove(min(l))
    
    print("A soma do segundo maior valor com o segundo menor =", max(l)+min(l))
    
else:
    print("Erro. Dois ou mais valores são iguais")