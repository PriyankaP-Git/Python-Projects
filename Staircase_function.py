import turtle

def stairs(size, nbs):
    for i in range (0,nbs):
        t.forward(size)
        t.left(90)
        t.forward(size)
        t.right(90)
       # size = size - 10
    t.forward(size)

t = turtle.Turtle()

stairs(50, 5)

turtle.done()