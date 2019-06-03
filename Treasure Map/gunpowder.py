from turtle import *
from random import *

setup(800, 800)

speed("fastest")

for turtle in range(4):
    forward(100)
    left(90)

forward(20)

def gunpowder():

    #keg base
    def kegbase():
        setheading(0)
        width(2.5)
        color("saddle brown")
        fillcolor("sienna")
        begin_fill()
        for keg in range(2):
            forward(57.5)
            left(55)
            circle(80, 70)
            left(55)
        
        end_fill()
    
    #keg accents

    def kegaccent():
        z = -3
        width(2)
        for accent in range(7):
            forward(8.8)
            if z < 0:

                if z == -3:
                    left(305)
                    circle(80, -70)
                    circle(80, 70)
                    right(305)
                        
                else:
                    left(300)
                    circle(92, -60)
                    circle(92, 60)
                    right(300)
                    
            if z == 0:
                backward(5.6)
                left(90)
                forward(92)
                backward(92)
                right(90)
                backward(5.6)

            if z > 0:

                if z == 3:
                    left(55)
                    circle(80, 70)
                    circle(80, -70)
                    right(55)
                    
                else:
                    left(60)
                    circle(92, 60)
                    circle(92, -60)
                    right(60)
            
            z += 1

    kegbase()
    kegaccent()
    
    #reposition to draw iron bars
    
    pu()
    forward(8.8)
    left(62.5)
    circle(80, 20)
    setheading(180)

    pd()

    #bottom iron bar
    
    def ironbar():
        pencolor("dim grey")
        width(7.5)
        forward(77.6)
        backward(77.6)

    ironbar()
    
    pu()
    setheading(0)
    left(75)  
    circle(80, 30)
    setheading(180)

    pd()
    
    ironbar()

    pu()
    forward(40)
    left(90)
    forward(12)
    pd()

    pencolor("#E8A86E")
    width(2.5)
    fillcolor("#E8A86E")
    begin_fill()
    right(90)

    lengths_1 = [20, 17.2, 40, 17.2, 20]
    for lengths_1 in lengths_1:
        forward(lengths_1)
        left(90)

    right(90)   
    end_fill()

    pu()
    lengths_2 = [20, 18.8, 5.44]
    for lengths_2 in lengths_2:
        forward(lengths_2)
        left(90)
    pd()
    
    right(90)
    pencolor("#000000")
    write("XXX", font=("Arial", 12, "normal"))

    def home():
        pu()
        setheading(270)
        forward(37.11)
        right(90)
        forward(32.99)
        pd()
    home()
    print(pos())
    
gunpowder()
hideturtle()
done()



