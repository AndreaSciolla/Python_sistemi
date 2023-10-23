f = open("ES_20_PAG_73", "w")
lista = [i for i in range(11)]
tavola = [lista for _ in range (10)]
for x in range(0, 10):
    tavola[x] = [lista[i]*(x+1) for i in range(1, 11)]
f.write(tavola[x] for x in range (11))
f.close()