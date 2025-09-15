def b_sort(l: list[int]) -> list[int]:
    # adiciona a menor ao começo da lista
    lista = [min(l)]
    # remove da lista original
    l.remove(min(l))
    
    if l[0] < l[1]:
        lista.append(l[0])    
        lista.append(l[1])    
    else:
        lista.append(l[0])    
        lista.append(l[1])    
        
    return lista
    


print("Digite três valores:")
l = []
for _ in range(3):
    i = int(input())
    l.append(i)
    
print(b_sort(l))

