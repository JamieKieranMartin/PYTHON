from turtle import *
from random import *

setup(800, 800)


for rectangle in range(4):
    forward(100)
    left(90)

def bomb():
   
    pu()
    setheading(0)
    forward(50)
    pd()
    #draws the bomb circle
    def bombcircle():
        width(2.5)
        color("#313131")
        fillcolor("#423F42")
        begin_fill()
        setheading(0)
        circle(30, 540)
        end_fill()
        
    bombcircle()

    #draws the fuse
    def fuse():
        setheading(45)
        width(5)
        color("#D8C5AF")
        circle(15, 100)

    fuse()

    #draws the light
    def spark(): 
        shape("triangle")
        color("orange")
        fillcolor("orange")
        turtlesize(1)
        speed("fastest")
        for outerspark in range(10):
            setheading(randint(1,359))
            stamp()
            
        color("yellow")
        fillcolor("yellow")
        turtlesize(0.5)
        for innerspark in range(5):
            setheading(randint(1,359))
            stamp()

    spark()

    def home():
        pu()
        setheading(270)
        forward(82.89)
        right(90)
        forward(48)
        pd()
    home()
    print(pos())


bomb()

    
    
hideturtle()
done()


