'''Il nostro amico Bob dopo alcune commissioni in giro per la città di Flatland deve rientrare a
casa. Purtroppo Bob soffre di momentanee perdite di memoria!
Questa volta la sua amnesia dura ben 60 minuti e durante questi 60 minuti Bob adotta la
seguente strategia per tentare di rientrare a casa. Ogni minuto decide a caso tra:
1. procedere 10 m verso Nord
2. procedere 10 m verso Sud
3. procedere 10 m verso Est
4. procedere 10 m verso Ovest
Simula l’intero percorso compiuto da Bob, supponendo che il punto di partenza abbia
coordinate (0,0) e salvalo all’interno di un dizionario opportunamente strutturato.
Disegna il percorso compiuto da Bob dentro una schermata di pygame oppure turtle, decidi
tu quale libreria usare.
Infine salva il percorso di Bob dentro un file .csv opportunamente strutturato.
BONUS: ogni volta in cui Bob passa in un punto della città di Flatland in cui è già passato,
stampa a schermo le coordinate del punto.'''


import random
import turtle
import csv

lung = 10

def disegna(alice, point):
    alice.pendown()
    alice.goto(point.x, point.y)

def calc_point(dire, punto):
    x, y = punto[0], punto[1]
    if dire == 0: #nord
        y += lung
    elif dire == 1: #est
        x += lung
    elif dire == 2: #sud 
        y -= lung
    elif dire == 3: #ovest
        x -= lung
    point = Point(x, y)
    return point

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def stampa(self):
        return f"({self.x},{self.y})"
    def compareTo(self, punto):
        if punto.x == self.x and punto.y == self.y:
            return True
        return False

def main():

    finestra = turtle.Screen()
    alice = turtle.Turtle()
    alice.goto(0,0)
    path = {0: Point(0,0)}
    direzioni = [0, 1, 2, 3]
    for time in range(1,60):
        dire = random.choice(direzioni)
        point = calc_point(dire, alice.pos())
        path[time] = point
        disegna(alice, point)
        for i in range(1,time):
            if point.compareTo(path[i]):
                print(f"gia passato: {point.stampa()}")

    with open("percorso.csv", "w") as file:
        file.write("MINUTO\t" + "X\t" + "Y\n")
        for minuto in path:
            file.write(str(minuto) + "\t" + str(path[minuto].x) +  "\t" + str(path[minuto].y) + "\n")
            
    finestra.mainloop()

if __name__ == "__main__":
    main()
