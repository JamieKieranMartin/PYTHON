from turtle import *
from random import *

setup(800, 800)

width(1)
for rectangle in range(4):
    forward(100)
    left(90)


def rum():
    forward(30)
    left(90)
    forward(1)
    right(90)
    color("#222334")
    width(2.5)
    begin_fill()
    fillcolor("#8CB8B8")

    def decoder(command):
        for command in command:
            action = command[0]
            if action == 'forward':
                pd()
                length = command[1]
                angle = command[2]
                forward(length)
                left(angle)
            elif action == 'circle':
                diameter = command[1][0]
                r_angle = command[1][1]
                angle = command[2]
                circle(diameter, r_angle)
                left(angle)
            elif action == 'goto':
                pu()
                length = command[1]
                angle = command[2]
                forward(length)
                left(angle)
            else:
                print("Don't understand!")
    
    #draws bottle and fills
    commands_1 = [['forward', 38, 45],
                 ['circle', [38, 110], 295],
                 ['forward', 30.5, 90],
                 ['forward', 17.5, 90],
                 ['forward', 30.5, 295],
                 ['circle', [38, 110], 0]]

    decoder(commands_1)
 
    setheading(0)
    end_fill()

    #repositions to draw cork
    commands_2 = [['goto', 38, 45],
                 ['circle', [38, 110], 295],
                 ['goto', 30.5, 90]]
    decoder(commands_2)

    #draw cork and fill
    begin_fill()
    fillcolor("#82582A")
    commands_3 = [['forward', 1.9, 270],
                 ['forward', 7.6, 90],
                 ['forward', 11.5, 90],
                 ['forward', 7.6, 270],
                ['forward', 0.5, 0]]
    decoder(commands_3)
    end_fill()

    #draw the glass accent and go to position of label
    pencolor("#E2FEFF")
    commands_4 = [['goto', 0.5, 90],
                  ['goto', 1.9, 0],
                  ['forward', 30, 295],
                  ['circle', [36, 110], 0],
                  ['goto', 0, 0],
                  ['circle', [36, -74], 119],
                  ['goto', 3.8, 0]
                  ]
    decoder(commands_4)

    #draw label
    pd()
    begin_fill()
    fillcolor("#E8A86E")
    pencolor("#000000")
    for label in range(2):
        forward(40)
        right(90)
        forward(20)
        right(90)   
    end_fill()
    
    #reposition to draw RUM text
    commands_5 = [['goto', -23, 90],
                  ['goto', -3.8, 270],
                  ['goto', 4, 0]
                  ]
    setheading(90)
    decoder(commands_5)

    pd()
    write("RUM", font=("Arial", 12, "normal"))

    def home():
        pu()
        setheading(270)
        forward(26.74)
        right(90)
        forward(33)
        pd()
        print(pos())
    home()
rum()
hideturtle()
done()



