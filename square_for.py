import turtle

def square(size):
    for i in range(0,4):
        t.forward(size)
        t.left(90)

t = turtle.Turtle()

square(100)
square(50)
square(10)

turtle.done()