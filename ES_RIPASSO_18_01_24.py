
class Testo():
    def __init__(self, testo, chiave, chiaro, n):  #chiaro se è true la parola è in chiaro
        self.testo = testo
        self.chiave = chiave
        self.chiaro = chiaro
        self.N = n
        testo_cript = ""
        testo_chiaro = ""

    def cifra(self, lett2num, num2lett):
        if self.chiaro:
            testo_cript = ""
            for lt, lc in zip(self.testo, self.chiave):
                num = (lett2num[lt] + lett2num[lc]) % self.N
                self.testo_cript += num2lett[num]
            print(f"il testo: '{self.testo}' criptato e': '{testo_cript}'")
            self.chiaro = False
        else:
            print("gia cifrato")

    def deCifra(self, lett2num, num2lett):
        if not self.chiaro:
            testo_chiaro = ""
            for lt, lc in zip(self.testo, self.chiave):
                num = (lett2num[lt] - lett2num[lc]) % self.N
                self.testo_chiaro += num2lett[num]
            print(f"il testo criptato: '{self.testo}' in chiaro e': '{testo_chiaro}'")
            self.chiaro = True
        else:
            print("gia chiaro")
def main():

    lett2num = {}
    num2lett = {}
    letters = "abcdefghilmnopqrstuvz ?"
    N = len(letters)
    for i, c in enumerate(letters):
        lett2num[c] = i
        num2lett[i] = c


    chiave = "itisdelpozzoprova"
    testo_cript = ""
    
    testo_c = str(input("inserisci parola: "))
    chiaro = bool(input("inserisci 0 = false, 1 = true, se la parola è in chiaro: "))
    testo = Testo(testo_c, "cfief", chiaro, N)
    testo.cifra(lett2num , num2lett)
    testo.deCifra(lett2num , num2lett)
    

if __name__ == "__main__":
    main()




