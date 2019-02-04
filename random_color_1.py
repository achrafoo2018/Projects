import turtle
from random import randint

colors = ['blue','purple','red','yellow','orange','green']
tr = turtle.Pen()
tr.speed(100)
turtle.bgcolor("black")
for x in range(330):
        tr.pencolor(colors[randint(0,5)])
        tr.width(x/100+1)
        tr.forward(x)
        tr.left(300)
        
turtle.done()

