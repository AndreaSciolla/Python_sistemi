class Quadrato():

    def __init__(self, lato, x, y): 
        self.lato = lato
        self.x = x
        self.y = y
    def calcolaArea(self):
        return self.lato**2
    def calcolaPer(self):
        return self.lato*4
    def isEsterno(self, punto):
        xp = int(punto[0])
        yp = int(punto[3])
        return !(xp <= self.x + self.lato and xp >= self.x and  yp <= self.y + self.lato and yp >= self.y)

def main():

    lato = int(input("inserisci il lato del quadrato: "))
    coord = input("inserisci le coordinate del vertice in basso a sinistra del quadrato (x, y): ")
    x = int(coord[0])
    y = int(coord[3])
    q = Quadrato(lato, x, y)
    punto = input("inserisci un punto sul piano (x, y): ") 
    if q.isEsterno(punto):
        print(f"il punto ({punto}) è esterno al quadrato")
    else:
        print(f"il punto ({punto}) è interno al quadrato")
    

if __name__ == "__main__":
    main()