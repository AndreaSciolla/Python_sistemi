

class Stringa():
    def __init__(self, parola, parola_divisa):
        self.parola = parola
        self.parola_divisa = parola_divisa

    def dividi(self):
        self.parola_divisa = [c for c in self.parola]
    def unisci(self):
        self.parola = ",".join(self.parola_divisa)


def scrivi_su_file(parola, parola_divisa):
    with open("es_verifica_prova.txt", "w") as f:
        f.write(parola)
        f.writelines(parola_divisa) # passo una lista e la scrive (con write non funge)

def main():
    parola = input("inserisci una parola: ")
    p_div = []
    stringa = Stringa(parola, p_div)
    stringa.dividi()
    stringa.unisci()
    scrivi_su_file(stringa.parola, stringa.parola_divisa)
    print(stringa.parola, stringa.parola_divisa)





if __name__ == "__main__":
    main()