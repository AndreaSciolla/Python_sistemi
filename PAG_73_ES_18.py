import math

lista = [i for i in range(0, 200) if(math.sqrt(i) % 1 == 0 and i % 2 != 0)]
print(lista)