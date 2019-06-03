from turtle import *

setup(800, 800)

def chest():
    #draw gold trim and chest box
    pu()
    setheading(0)
    forward(2)
    left(90)
    forward(5)
    right(90)
    pd()
    
    def trimandbox():
        width(3.2)
        color("gold")
        fillcolor("sienna")
        begin_fill()
        for square in range(2):
            forward(96)
            left(90)
            dot(4.8)
            forward(64)
            left(90)
            dot(4.8)
        end_fill()

    trimandbox()
    
    #draw chest brown accents and gold lid trim

    def accents():
        z = 0
        #-----START FOR IN-----
        for lid in range(3):
            z += 12.8
            print(z)
            #when the turtle hits a certain height, draw gold lid trim
            if z == 38.400000000000006:
                color("gold")
                width(3.2)
                left(90)
                forward(z)
                right(90)
                pd()
                forward(48)

                #draw keyhole
                dot(12.8)
                pu()
                right(90)
                forward(1.6)
                pd()
                color('black')
                shape('triangle')
                setheading(90)
                turtlesize(0.32)
                stamp()
                forward(3.2)
                dot(6.4)
                backward(1.6)
                setheading(0)
                pu()
                forward(4.8)
                pd()

                #continue gold lid trim
                color('gold')
                forward(43.2)

                #go back to start
                pu()
                backward(96)
                left(90)
                backward(z)
                right(90)
                
                
                z += 12.8

            #brown accents   
            color("saddle brown")
            pu()
            left(90)
            forward(z)
            right(90)
            forward(3.2)
            width(1.6)
            pd()
            forward(89.6)
            backward(89.6)
            pu()

            pu()
            backward(3.2)
            left(90)
            backward(z)
            right(90)
            pd()

            

        #-----END FOR IN-----

    accents()
    
    # draw vertical gold trim

    def goldtrim():
        y = 19.2
        #-----START FOR IN-----
        for accent in range (2):
            
            setheading(0)
            pd()
            width(3.2)
            color('gold')
            forward(y)
            left(90)
            forward(38.4)
            pu()

            backward(38.4)
            right(90)
            backward(y)

            
            y += 57.
        #-----END FOR IN-----

    goldtrim()
    def home():
        pu()
        setheading(270)
        forward(5)
        right(90)
        forward(2)
        pd()
        print(pos())
    home()

chest()
hideturtle()
done()
