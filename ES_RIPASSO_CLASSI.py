import random

class Nemico():
    def __init__ (self, pos_x, pos_y, n_vite):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.n_vite = n_vite
    def stampa(self):
        print(f"Nemico in posizione {self.pos_x}, {self.pos_y} con {self.n_vite} vite")    
    
def main():
    N_NEMICI = 5
    WIDTH = 800
    HEIGHT = 400
    lista_nemici = []
    random.seed(1234)  #seme del generatore di numeri pseudo casuali (se lasci quello esce sempre lo stesso numero)
    for _ in range(N_NEMICI):
        pos_x = random.randint(0, WIDTH - 1)#randint include gli estremi quindi si fa -1
        pos_y = random.randint(0, HEIGHT - 1)#randint include gli estremi quindi si fa -1
        nemico = Nemico(pos_x, pos_y, 5)
        lista_nemici.append(nemico)

    personaggio = {"posizione_x": 100, "posizione_y": 200}
    for nemico in lista_nemici:
        nemico.stampa()
        if (nemico.pos_x == personaggio["posizione_x"] and nemico.pos_y == personaggio["posizione_y"]):
            print("collisione")


if __name__ == "__main__":
    main()