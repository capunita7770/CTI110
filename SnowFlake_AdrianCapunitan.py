# SnowFlakes
# 6/22
# CTI-110 - SnowFlakes
# Adrian Capunitan
#

import turtle

win = turtle.Screen()
t = turtle.Turtle()
win.bgcolor("blue")

colors = ["cyan","purple","white","gray",]
for i in range (75):
        for i in range (2):
            t.forward(100)
            t.left(60)
            t.forward(100)
            t.left(120)
        t.left(25)
        

win.exitonclick()
