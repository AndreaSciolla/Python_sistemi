import turtle

def main():
    lato = 10
    finestra = turtle.Screen()
    sporgis = turtle.Turtle()
    sporgis.speed(1)
    for _ in range(0, 5):
        sporgis.forward(lato * 4)
        sporgis.penup()
        sporgis.goto(sporgis.xcor() - lato*4, sporgis.ycor() + lato)
        sporgis.pendown()
    sporgis.right(90)
    sporgis.penup()
    sporgis.forward(lato)
    sporgis.pendown()

    for _ in range(0, 5):
        sporgis.forward(lato * 4)
        sporgis.penup()
        sporgis.goto(sporgis.xcor() + lato , sporgis.ycor() + lato*4)
        sporgis.pendown()
    finestra.mainloop()

                        


if __name__ == "__main__":
    main()