import turtle
import time
t = turtle.Turtle()
turtle.screensize(1100,1100)
turtle.title("National Flag of Indial")

def rect(color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(2):
        t.forward(400)
        t.right(90)
        t.forward(100)
        t.right(90)
    t.end_fill()

t.up()
t.pensize(4)
t.goto(0,-300)
t.down()
t.goto(0,400)
rect("orange")

t.goto(0,300)
t.forward(200)
t.color("blue")
t.circle(-50)
t.setheading(270)
t.forward(50)
t.setheading(0)

for i in range(24):
    t.forward(45)
    t.bk(45)
    t.left(15)

t.setheading(90)
t.forward(50)
t.setheading(0)
t.color("black")
t.forward(200)
t.right(90)
t.forward(100)
t.right(90)
t.forward(400)
t.right(90)
t.forward(100)
t.right(90)
t.goto(0,200)
rect("green")

time.sleep(10)