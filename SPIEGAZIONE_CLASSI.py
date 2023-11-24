#SPIEGAZIONE CLASSI
#in python non c'è private o public -> tutto pubblico -> non ci sono set e get
#in python non si può fare l'overloading

class Quadrato():

    def __init__(self, lato):  #tutti i costruttori si chiamano init e bisogna mettere il parametro self (in tutti i metodi)
        self.lato = lato #self è come il this in  java
    def calcolaArea(self):
        return self.lato**2
    def stampaLato(self):
        print(f"lato: {self.lato}")

def main():

    q = Quadrato(4)  #per creare un'istanza di quadrato chiamo il nome della classe 
    print(f"l'area del quadrato è {q.calcolaArea()}")  #nelle chiamate non si passa il self
    q.stampaLato()

if __name__ == "__main__":
    main()