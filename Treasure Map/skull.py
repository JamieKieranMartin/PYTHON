from turtle import *
from random import *

setup(800, 800)
width(2.5)
speed("fast")

forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)
forward(100)
left(90)



def skull_bone():
    #centers the skull in a 100 by 100 box
    def center():
        pu()
        forward(25)
        left(90)
        forward(20)
        pd()
    center()
    #draw bones
    def bones():
        setheading(45)
        x = 0
        for bone in range(4):
            forward(75)
            right(90)
            circle(5, 270)
            right(180)
            circle(5, 270)
            right(90)

            if x==1:
                setheading(0)
                pu()
                forward(53)
                left(90)
                forward(7.5)
                left(45)
                pd()

            x += 1

    bones()
    
    #reposition
    def reposition():
        pu()
        setheading(135)
        forward(25)
        left(135)
        pd()

    reposition()

    #skull shape
    def skull():
        begin_fill()
        fillcolor("white")
        
        forward(15)
        left(270)
        forward(25)
        left(270)
        forward(15)
        left(315)
        
        right(90)
        circle(17.5, -270)
        end_fill()
        setheading(270)
        forward(15)
        left(270)

    skull()

    #draw teeth
    def teeth():
        for teeth in range(4):
            forward(5)
            right(90)
            forward(5)
            backward(5)
            left(90)    
        

    teeth()
    #reposition and draw eyes
    def eyes():
        y=25
        for eyes in range(2):    
            left(270)
            pu()
            forward(y)
            pd()
            dot(10)
            y -= 10

    eyes()

    #goto the start
    def home():
        pu()
        right(90)
        forward(55.18)
        right(90)
        forward(55.07)
        pd()
        
    home()



skull_bone()

done()


