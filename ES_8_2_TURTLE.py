import turtle
#stampare i primi 9 poligoni sulla finestra

def disegnaPoligono(t, num, lato):
    for k in range(0, i):
        alice.left(360/i)
        alice.forward(lato/i)

#def posizionaTurtle():
    

def main():

    finestra = turtle.Screen()
    alice = turtle.Turtle()
    alice.shape("turtle")
    alice.color('red', 'blue')#cambia il colore della linea
    per = 400
    alice.penup()
    alice.backward(150)
    alice.left(90)
    alice.forward(150)
    alice.right(90)
    alice.pendown()
    for i in range(3, 12):
        alice.pendown()
        disegnaPoligono(alice, i, per)
        alice.penup()
        alice.forward(150)
        if i != 3:
            if ((i-2)%3)== 0:
                alice.penup()
                alice.right(90)
                alice.forward(155)
                alice.left(90)
                alice.backward(470)
    finestra.mainloop()
if __name__ == "__main__":
    main()