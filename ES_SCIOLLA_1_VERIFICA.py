'''ESERCIZIO 1 VERIFICA DI SISTEMI'''

class Testo():
    def __init__(self, frase):
        self.frase = frase
        self.dividi_split = [] #messa qui perche la uso in piu metodi

    def calc_lung(self):
        return len(self.frase)

    def dividi(self):
        self.dividi_split =  self.frase.split(" ")
        return self.dividi_split
    
    def calc_lung_parole(self):  #potevi fare list comprehension
        cont_lung_parole = []
        for parola in self.dividi_split:
            cont_lung_parole.append(len(parola))
        return cont_lung_parole

    def cerca_parola(self, parola):  #return parola in self.lista
        for p in self.dividi_split:
            if p == parola:
                return True
        return False

    def salva_su_file(self): #puoi mettere nomefile
        with open("es_1_sciolla_verifica.txt", "w") as f:
            f.write(self.frase)

    def diz_frequenze(self):
        diz = {}
        for p in self.dividi_split: #scorre le parole e le mette in un dizionario come chiavi
            if p not in diz:
                diz[p] = 1
            else:
                diz[p]+= 1
        return diz


def main():

    testo = input("inserisci il testo: ")
    t = Testo(testo)
    print(f"lunghezza testo:  {t.calc_lung()}")
    print(f"testo diviso:  {t.dividi()}")
    print(f"lunghezza parole:  {t.calc_lung_parole()}")
    parola = input("\ninserisci una parola da cercare: ")
    if (t.cerca_parola(parola)):
        print("\nparola presente nel testo")
    else:
        print("\nparola non e' presente nel testo")
    print(t.diz_frequenze())
    t.salva_su_file()

if __name__ == "__main__":
    main()