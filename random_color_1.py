import turtle
from random import randint

colors = ['blue','purple','red','yellow','orange','green']
tr = turtle.Pen()
tr.speed(100)
turtle.bgcolor("black")
for i in range(330):
        tr.pencolor(colors[randint(0,5)])
        tr.width(i/150)
        tr.forward(x)
        tr.left(300) # Change This Value And Enjoy :D
        
turtle.done()

