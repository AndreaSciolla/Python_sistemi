''' 
CIFRARIO VERNAM
ci sono 21 lettere minuscole
per tradurre lettere in numeri:
a = 0
b = 1
c = 2
...
per codificare bisogna avere una chiave -> può essere una stringa (lunga almeno quanto il mio testo)
come funziona algoritmo:
- tradurre lettere in numeri (sia di parola che di chiave)
- sommare numeri della parola con quelli della chiave
- tradurre somma in lettere -> parola codificata
ATTENZIONE:
dopo aver fatto la somma fare % 21 (numero di lettere disponibili) -> cosi siamo sicuri che il valore arriva al massimo a 20

fare una classe -> quando la istanziamo possono contenere sia un testo in chiaro che codificato

'''
class Testo():
    def __init__(self, testo, chiave, chiaro):  #chiaro se è true la parola è in chiaro
        self.testo = testo
        self.chiave = chiave
        self.chiaro = chiaro

    def cifra(self, diz_l_n, diz_n_l):
        if self.chiaro:
            somma = []
            testo_c = ""
            for cl, cc in zip(self.testo, self.chiave):
                somma.append((diz_l_n[cl] + diz_l_n[cc]) % 21)
            for i in somma:
                testo_c += diz_n_l[i] 
            print(testo_c)
            self.chiaro = False
        else:
            print("gia cifrato")
    def deCifra(self, diz_l_n, diz_n_l):
        if not self.chiaro:
            somma = []
            testo_c = ""
            for cl, cc in zip(self.testo, self.chiave):
                somma.append((diz_l_n[cl]) % 21)
            for i in somma:
                testo_c += diz_n_l[i] 
            print(testo_c)
            self.chiaro = True
        else:
            print("gia cifrato")
def main():
    diz_lett_to_num = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'l': 9, 'm': 10, 'n': 11, 'o': 12, 'p': 13, 'q': 14, 'r': 15, 's': 16, 't': 17, 'u': 18, 'v': 19, 'z': 20, }
    diz_num_to_lett = {}
    for chiave in diz_lett_to_num:
        diz_num_to_lett[diz_lett_to_num[chiave]] = chiave
    parola = str(input("inserisci parola: "))
    chiaro = bool(input("inserisci 0 = false, 1 = true, se la parola è in chiaro: "))
    testo = Testo(parola, "cfief", chiaro)
    testo.cifra(diz_lett_to_num, diz_num_to_lett)
    testo.deCifra(diz_lett_to_num, diz_num_to_lett)
    

if __name__ == "__main__":
    main()




