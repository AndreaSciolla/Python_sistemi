import turtle
LUNG = 100

def nord(alice):
    alice.setheading(90)
    alice.forward(LUNG)

def sud(alice):
    alice.setheading(270)
    alice.forward(LUNG)

def est(alice):
    alice.setheading(0)
    alice.forward(LUNG)

def ovest(alice):
    alice.setheading(180)
    alice.forward(LUNG)   

def main():

    finestra = turtle.Screen()
    alice = turtle.Turtle()
    alice.shape("turtle")
    direzioni = {"n": nord, "s": sud, "e": est, "o": ovest, "exit": exit}
    while True:
        direzione = (input("inseirsici direzione[n, s, e, o] esc per uscire: "))
        if direzione in direzioni:
            direzioni[direzione](alice)
    finestra.mainloop()
if __name__ == "__main__":
    main()