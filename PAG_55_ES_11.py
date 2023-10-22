x = [0, 1, 2, 3, 5, 6, 7, 8]
lung = len(x)
mezzo = lung//2
lista1 = x[:mezzo]
lista2 = x[mezzo:]
lista1.append(lista2[0])
print(lista1)
print(lista2)
