import turtle

num = int(input("inserisci il numero di lati:"))
lato = int(input("inserisci il lati del poligono:"))
gradi = 360/num
finestra = turtle.Screen()
alice = turtle.Turtle()
alice.color('red', 'blue')
alice.begin_fill()

for i in range(0, num):
    alice.left(gradi)
    alice.forward(lato)
alice.end_fill() 

finestra.mainloop()