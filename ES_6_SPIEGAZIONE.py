import turtle #esempio di importazione di un modulo built_in -> vuol dire che è nativo (presente dentro python)
#turtle implementa il linguaggio LOGO

finestra = turtle.Screen() #creo la finestra grafica
alice = turtle.Turtle() #creo il cursore
alice.forward(100)#il cursore si muove di 100 px
alice.left(30)
alice.forward(50)


finestra.mainloop() #serve per tenere sempre aperta la finestra