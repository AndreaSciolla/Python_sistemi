import turtle

class barcode():
    def __init__(self):
        stringa = input("inserisci una stringa di 8 caratteri: ")
        while len(stringa) != 8:
            stringa = input("NON VALIDA!! reinserisci una stringa di 8 caratteri: ")
        self.stringa = stringa
        self.listaBin = []
    
    def completa8bit(self, strbin):
        b = strbin[2:]
        l = len(b)
        return "0" * (8 - l) + b

    def trasformaSbinario(self):
        for k in self.stringa:
            asci = ord(k)
            if asci <= 255:
                asci_bin = bin(asci)
                self.listaBin.append(self.completa8bit(asci_bin))
        
    def stampaAsci(self):
        print(self.stringa)
        print(self.listaBin)

    def disegnaCodiceBarre(self):
        finestra = turtle.Screen()
        sporgis = turtle.Turtle()
        sporgis.speed(0)
        sporgis.penup()
        for byte in self.listaBin:
            for bit in byte:
                if bit == "1":
                    sporgis.pendown()
                sporgis.width(4)
                sporgis.setheading(90)
                sporgis.forward(100)
                sporgis.penup()
                sporgis.right(90)
                sporgis.forward(5)
                sporgis.right(90)
                sporgis.forward(100)
        finestra.mainloop()
                        
def main():
        bc = barcode()
        bc.trasformaSbinario()
        bc.stampaAsci()
        bc.disegnaCodiceBarre()

if __name__ == "__main__":
    main()