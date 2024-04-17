import random
import turtle
scn=turtle.Screen()
colors = ["#98FB98", "#7FFFD4", "#CD853F", "#2F4F4F", "#800000" , "#191970", "#5F9EA0", "#556B2F", "#BA55D3"]


class ShapeFactory():
    def __init__(self):
        self.geo=turtle.Turtle()
        self.geo.hideturtle()
        self.geo.pu()
        self.geo.goto(random.randint(-400, 400), random.randint(-400, 400))
        self.geo.pd()
        self.geo.speed(500)


    def circle(self):
        r = random.randint(20,50)
        self.geo.fillcolor(random.choice(colors))
        self.geo.begin_fill()
        self.geo.circle(r)
        self.geo.end_fill()


    def triangle(self):
        self.geo.fillcolor(random.choice(colors))
        self.geo.begin_fill()
        t = random.randint(20, 100)
        for o in range(0, 3, 1):
            self.geo.fd(t)
            self.geo.rt(120)
        self.geo.end_fill()


    def rectangle(self):
        u = random.randint(20,100)
        self.geo.fillcolor(random.choice(colors))
        self.geo.begin_fill()
        for o in range(0, 4, 1):
            self.geo.fd(u)
            self.geo.rt(90)
        self.geo.end_fill()


for i in range(0, 100):
    George = ShapeFactory()
    shape = random.randint(1, 3)
    if shape==1:
        George.circle()
    elif shape==2:
        George.triangle()
    elif shape==3:
        George.rectangle()





