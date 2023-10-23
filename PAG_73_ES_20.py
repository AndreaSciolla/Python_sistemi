f = open("ES_20_PAG_73.txt", "w")
lista = [[k*i for k in range(1, 11)] for i in range(1, 11)]
for k,tabellina in enumerate(lista): #la funzione enumerate ritorna indice della lista e il suo elemento
    #tabellina è una lista, 'lista' è una lista di liste
    #print(f"tabellina del {k+1}:  {tabellina}")
    f.write(f"tabellina del {k+1}:  {tabellina} \n")
f.close()