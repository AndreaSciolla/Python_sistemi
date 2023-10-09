import turtle
#stampare i primi 9 poligoni sulla finestra

finestra = turtle.Screen()
alice = turtle.Turtle()
alice.color('red', 'blue')
alice.begin_fill()
per = 400
alice.penup()
alice.backward(150)
alice.left(90)
alice.forward(150)
alice.right(90)
alice.pendown()
for i in range(3, 12):
    alice.pendown()
    for k in range(0, i):
        alice.left(360/i)
        alice.forward(per/i)
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