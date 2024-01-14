def main():

    #DIZIONARI

    dizionario = {"a": "albero", "b": "brutto", "c": "casa"}
    lista = ["albero", "brutto", "casa"]
    #print(dizionario["b"])
    dizionario["d"] = "dado"  #aggiungo elemento 
    dizionario["a"] = "alto"  #sovrascrive elemento 
    #print(dizionario)

    #ciclo su dizionario

    for chiave in dizionario:
        print(chiave)  #stampa solo le chiavi

    for chiave in dizionario:
        print(dizionario[chiave])  #stampa solo i valori

    if "a" in dizionario:   #verifica se una chiave è presente in dizionario in dizionario
        print("a è presente in dizionario")

if __name__ == "__main__":
    main()