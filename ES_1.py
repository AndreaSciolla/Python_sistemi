def main(): #in python i blocchi dipendono dall'indentazione
    nome = input("come ti chiami?")  
    anni = int(input("quanti anni hai?"))    #la funzione input restituisce solo stringhe      #quindi anni è una variabile di tipo stringa
    anno_corrente = int(input("in quale anno siamo")) #se metto int converto stringa in intero
    print(f"ti chiami {nome} e hai {anni} anni")       
    print(f"sei nato nel {anno_corrente - anni}")
    #la funzione type() restituisce il tipo di una variabile



if __name__ == "__main__":  #attenzione al doppio underscore (doubleunder) -> dunder __name__ si legge: "dander neim dander"
    main()