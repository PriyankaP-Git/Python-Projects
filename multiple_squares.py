import turtle

def square(size):
    for i in range(0,4):
        t.forward(size)
        t.left(90)

def squares(beginning_size, nbs):
    for i in range(0,nbs):
        size = (i+1) * beginning_size
        square(size)
        #t.left(5)

t = turtle.Turtle()

squares(10, 10)

turtle.done()