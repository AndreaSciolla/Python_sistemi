#DISEGNARE UNA STELLA A N PUNTE
import turtle
import math

n = int(input("inserisci il numero di punte: "))
finestra = turtle.Screen()
alice = turtle.Turtle()
lato = 200

alice.color('red', 'blue')
alice.begin_fill()

if n != 0 and n !=1:
    if(n%2)!=0:
        for i in range(0, n):
            alice.forward(lato)
            alice.left(720/n)
    else:
        for k in range(0, int(n/2)):
            alice.forward(lato)
            alice.left(720/n)
        alice.penup()
        alice.forward(lato/2)
        alice.right(90)
        alice.forward(((lato/3)/math.sqrt(2))/(n/8))  #formula per  trovale cateto del mezzo triangolo che forma punta della stella
        alice.left(360/n + 90)
        alice.pendown()
        for j in range(0, int(n/2)):
            alice.forward(lato)
            alice.left(720/n)
   

else:
    print("il numero di punte inserito non è valido")

alice.end_fill()
finestra.mainloop()