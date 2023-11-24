def contaLettera(stringa):
    dizionario = {"A": 0, "T": 0, "G": 0, "C": 0, }
    for c in stringa:
        dizionario[c] += 1
    return dizionario

def main():

    f = open("covid-19_gen1.txt", "r")
    stringa = ""
    sequenza = "ATGTTTGTTTTT"
    for riga in f.readlines():
        stringa += riga[0:-1]
    f.close()
    
    print(contaLettera(stringa))
    print(stringa.find(sequenza))
    
        
if __name__ == "__main__":
    main()