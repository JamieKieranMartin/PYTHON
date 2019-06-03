
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: n10212361
#    Student name: Jamie Martin
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  All files submitted will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/).
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  TREASURE MAP
#
#  This assignment tests your skills at processing data stored in
#  lists, creating reusable code and following instructions to display
#  a complex visual image.  The incomplete Python program below is
#  missing a crucial function, "follow_path".  You are required to
#  complete this function so that when the program is run it traces
#  a path on the screen, drawing "tokens" to indicate discoveries made
#  along the way, while using data stored in a list to determine the
#  steps to be taken.  See the instruction sheet accompanying this
#  file for full details.
#
#  Note that this assignment is in two parts, the second of which
#  will be released only just before the final deadline.  This
#  template file will be used for both parts and you will submit
#  your final solution as a single Python 3 file, whether or not you
#  complete both parts of the assignment.
#
#--------------------------------------------------------------------#  



#-----Preamble-------------------------------------------------------#
#
# This section imports necessary functions and defines constant
# values used for creating the drawing canvas.  You should not change
# any of the code in this section.
#

# Import the functions needed to complete this assignment.  You
# should not need to use any other modules for your solution.  In
# particular, your solution must not rely on any non-standard Python
# modules that need to be downloaded and installed separately,
# because the markers will not have access to such modules.

from turtle import *
from math import *
from random import *

# Define constant values used in the main program that sets up
# the drawing canvas.  Do not change any of these values.

grid_size = 100 # pixels
num_squares = 7 # to create a 7x7 map grid
margin = 50 # pixels, the size of the margin around the grid
legend_space = 400 # pixels, the space to leave for the legend
window_height = grid_size * num_squares + margin * 2
window_width = grid_size * num_squares + margin +  legend_space
font_size = 18 # size of characters for the coords
starting_points = ['Top left', 'Top right', 'Centre',
                   'Bottom left', 'Bottom right']

#
#--------------------------------------------------------------------#



#-----Functions for Creating the Drawing Canvas----------------------#
#
# The functions in this section are called by the main program to
# manage the drawing canvas for your image.  You should not change
# any of the code in this section.  (Very keen students are welcome
# to draw their own background, provided they do not change the map's
# grid or affect the ability to see it.)
#

# Set up the canvas and draw the background for the overall image
def create_drawing_canvas():
    
    # Set up the drawing window with enough space for the grid and
    # legend
    setup(window_width, window_height)
    setworldcoordinates(-margin, -margin, window_width - margin,
                        window_height - margin)

    # Draw as quickly as possible
    tracer(False)

    # Choose a neutral background colour (if you want to draw your
    # own background put the code here, but do not change any of the
    # following code that draws the grid)
    bgcolor('light grey')

    # Get ready to draw the grid
    penup()
    color('slate grey')
    width(2)

    # Draw the horizontal grid lines
    setheading(0) # face east
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(0, y_coord)
        pendown()
        forward(num_squares * grid_size)
        
    # Draw the vertical grid lines
    setheading(90) # face north
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        penup()
        goto(x_coord, 0)
        pendown()
        forward(num_squares * grid_size)

    # Draw each of the labels on the x axis
    penup()
    y_offset = -27 # pixels
    for x_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_coord, y_offset)
        write(str(x_coord), align = 'center',
              font=('Arial', font_size, 'normal'))

    # Draw each of the labels on the y axis
    penup()
    x_offset, y_offset = -5, -10 # pixels
    for y_coord in range(0, (num_squares + 1) * grid_size, grid_size):
        goto(x_offset, y_coord + y_offset)
        write(str(y_coord), align = 'right',
              font=('Arial', font_size, 'normal'))

    # Mark the space for drawing the legend
    goto((num_squares * grid_size) + margin, (num_squares * grid_size) // 2)
    write('    Legend', align = 'left',
          font=('Arial', 24, 'normal'))
        
    # Reset everything ready for the student's solution
    pencolor('black')
    width(1)
    penup()
    home()
    tracer(True)


# End the program and release the drawing canvas to the operating
# system.  By default the cursor (turtle) is hidden when the
# program ends - call the function with False as the argument to
# prevent this.
def release_drawing_canvas(hide_cursor = True):
    tracer(True) # ensure any drawing still in progress is displayed
    if hide_cursor:
        hideturtle()
    done()
    
#
#--------------------------------------------------------------------#



#-----Test Data for Use During Code Development----------------------#
#
# The "fixed" data sets in this section are provided to help you
# develop and test your code.  You can use them as the argument to
# the follow_path function while perfecting your solution.  However,
# they will NOT be used to assess your program.  Your solution will
# be assessed using the random_path function appearing below.  Your
# program must work correctly for any data set that can be generated
# by the random_path function.
#
# Each of the data sets is a list of instructions expressed as
# triples.  The instructions have two different forms.  The first
# instruction in the data set is always of the form
#
#     ['Start', location, token_number]
#
# where the location may be 'Top left', 'Top right', 'Centre',
# 'Bottom left' or 'Bottom right', and the token_number is an
# integer from 0 to 4, inclusive.  This instruction tells us where
# to begin our treasure hunt and the token that we find there.
# (Every square we visit will yield a token, including the first.)
#
# The remaining instructions, if any, are all of the form
#
#     [direction, number_of_squares, token_number]
#
# where the direction may be 'North', 'South', 'East' or 'West',
# the number_of_squares is a positive integer, and the token_number
# is an integer from 0 to 4, inclusive.  This instruction tells
# us where to go from our current location in the grid and the
# token that we will find in the target square.  See the instructions
# accompanying this file for examples.
#

# Some starting points - the following fixed paths just start a path
# with each of the five tokens in a different location

fixed_path_0 = [['Start', 'Top left', 0]]
fixed_path_1 = [['Start', 'Top right', 1]]
fixed_path_2 = [['Start', 'Centre', 2]]
fixed_path_3 = [['Start', 'Bottom left', 3]]
fixed_path_4 = [['Start', 'Bottom right', 4]]

# Some miscellaneous paths which encounter all five tokens once

fixed_path_5 = [['Start', 'Bottom right', 0], ['East', 1, 1], ['East', 1, 2],
                ['East', 1, 3], ['East', 1, 4]]
fixed_path_6 = [['Start', 'Bottom right', 0], ['West', 1, 1], ['West', 1, 2],
                ['West', 1, 3], ['West', 1, 4]]
fixed_path_7 = [['Start', 'Centre', 4], ['North', 2, 3], ['East', 2, 2],
                ['South', 4, 1], ['West', 2, 0]]

# A path which finds each token twice

fixed_path_8 = [['Start', 'Bottom left', 1], ['East', 5, 2],
                ['North', 2, 3], ['North', 4, 0], ['South', 3, 2],
                ['West', 4, 0], ['West', 1, 4],
                ['East', 3, 1], ['South', 3, 4], ['East', 1, 3]]

# Some short paths

fixed_path_9 = [['Start', 'Centre', 0], ['East', 3, 2],
                ['North', 2, 1], ['West', 2, 3],
                ['South', 3, 4], ['West', 4, 1]]

fixed_path_10 = [['Start', 'Top left', 2], ['East', 6, 3], ['South', 1, 0],
                 ['South', 1, 0], ['West', 6, 2], ['South', 4, 3]]

fixed_path_11 = [['Start', 'Top left', 2], ['South', 1, 0], ['East', 2, 4],
                 ['South', 1, 1], ['East', 3, 4], ['West', 1, 3],
                 ['South', 2, 0]]

# Some long paths

fixed_path_12 = [['Start', 'Top right', 2], ['South', 4, 0],
                 ['South', 1, 1], ['North', 3, 4], ['West', 4, 0],
                 ['West', 2, 0], ['South', 3, 4], ['East', 2, 3],
                 ['East', 1, 1], ['North', 3, 2], ['South', 1, 3],
                 ['North', 3, 2], ['West', 1, 2], ['South', 3, 4],
                 ['East', 3, 0], ['South', 1, 1]]

fixed_path_13 = [['Start', 'Top left', 1], ['East', 5, 3], ['West', 4, 2],
                 ['East', 1, 3], ['East', 2, 2], ['South', 5, 1],
                 ['North', 2, 0], ['East', 2, 0], ['West', 1, 1],
                 ['West', 5, 0], ['South', 1, 3], ['East', 3, 0],
                 ['East', 1, 4], ['North', 3, 0], ['West', 1, 4],
                 ['West', 3, 1], ['South', 4, 1], ['East', 5, 1],
                 ['West', 4, 0]]

# "I've been everywhere, man!" - this path visits every square in
# the grid, with randomised choices of tokens

fixed_path_99 = [['Start', 'Top left', randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['West', 1, randint(0, 4)] for step in range(6)] + \
                [['South', 1, randint(0, 4)]] + \
                [['East', 1, randint(0, 4)] for step in range(6)]

# If you want to create your own test data sets put them here
 
#
#--------------------------------------------------------------------#



#-----Function for Assessing Your Solution---------------------------#
#
# The function in this section will be used to assess your solution.
# Do not change any of the code in this section.
#
# The following function creates a random data set specifying a path
# to follow.  Your program must work for any data set that can be
# returned by this function.  The results returned by calling this
# function will be used as the argument to your follow_path function
# during marking.  For convenience during code development and
# marking this function also prints the path to be followed to the
# shell window.
#
# Note: For brevity this function uses some Python features not taught
# in IFB104 (dictionaries and list generators).  You do not need to
# understand this code to complete the assignment.
#
def random_path(print_path = True):
    # Select one of the five starting points, with a random token
    path = [['Start', choice(starting_points), randint(0, 4)]]
    # Determine our location in grid coords (assuming num_squares is odd)
    start_coords = {'Top left': [0, num_squares - 1],
                    'Bottom left': [0, 0],
                    'Top right': [num_squares - 1, num_squares - 1],
                    'Centre': [num_squares // 2, num_squares // 2],
                    'Bottom right': [num_squares - 1, 0]}
    location = start_coords[path[0][1]]
    # Keep track of squares visited
    been_there = [location]
    # Create a path up to 19 steps long (so at most there will be 20 tokens)
    for step in range(randint(1,19)):
        # Find places to go in each possible direction, calculating both
        # the new grid square and the instruction required to take
        # us there
        go_north = [[[location[0], new_square],
                     ['North', new_square - location[1], token]]
                    for new_square in range(location[1] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_south = [[[location[0], new_square],
                     ['South', location[1] - new_square, token]]
                    for new_square in range(0, location[1])
                    for token in [0, 1, 2, 3, 4]
                    if not ([location[0], new_square] in been_there)]
        go_west = [[[new_square, location[1]],
                    ['West', location[0] - new_square, token]]
                    for new_square in range(0, location[0])
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        go_east = [[[new_square, location[1]],
                    ['East', new_square - location[0], token]]
                    for new_square in range(location[0] + 1, num_squares)
                    for token in [0, 1, 2, 3, 4]
                    if not ([new_square, location[1]] in been_there)]
        # Choose a free square to go to, if any exist
        options = go_north + go_south + go_east + go_west
        if options == []: # nowhere left to go, so stop!
            break
        target_coord, instruction = choice(options)
        # Remember being there
        been_there.append(target_coord)
        location = target_coord
        # Add the move to the list of instructions
        path.append(instruction)
    # To assist with debugging and marking, print the list of
    # instructions to be followed to the shell window
    print('Welcome to the Treasure Hunt!')
    print('Here are the steps you must follow...')
    for instruction in path:
        print(instruction)
    # Return the random path
    return path

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
#  Complete the assignment by replacing the dummy function below with
#  your own "follow_path" function.
#

# Follow the path as per the provided dataset

#-------------------------BEGINNING OF CHEST ICON----------------------------

def chest():
    #reposition turtle to fit chest in 100x100 box
    def reposition():
        pu()
        setheading(0)
        forward(2)
        left(90)
        forward(5)
        right(90)
        pd()
        
    reposition()
    #draw gold outline trim and chest box then fill
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
            #when the turtle hits a certain height, draw gold lid trim and keyhole
            if z == 38.400000000000006:
                #draw gold lid trim
                color("gold")
                width(3.2)
                left(90)
                forward(z)
                right(90)
                pd()
                forward(48)
                #draw keyhole circle and triangle
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
            #reposition to start of accent drawing each time it draws
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
            #move to position and draw vertical gold trim 
            setheading(0)
            pd()
            width(3.2)
            color('gold')
            forward(y)
            left(90)
            forward(38.4)
            pu()
            #go back to start
            backward(38.4)
            right(90)
            backward(y)

            y += 57
            
        #-----END FOR IN-----

    goldtrim()

#-------------------------------END OF CHEST ICON----------------------------


#-------------------------BEGINNING OF BOMB ICON----------------------------

#this function draws a bomb with a randomly generated spark
    
def bomb():
    setheading(0)
    #repositions to draw bomb
    def reposition():
        pu()
        setheading(0)
        forward(50)
        left(90)
        forward(3)
        pd()
        
    reposition()
    
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

    
#-------------------------------END OF BOMB ICON----------------------------


#-------------------------BEGINNING OF GUNPOWDER KEG ICON-----------------------

#this function draws a gunpowder keg
def gunpowder():
    #repositions turtle to draw gunpowder keg
    def reposition_1():
        setheading(0)
        pu()
        forward(21)
        left(90)
        forward(4)
        pd()
        
    reposition_1()
    
    #draws the base of the keg and fills with colour
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

    kegbase()
     
    #accents the keg to appear like wooden planks

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

    kegaccent()
    
    #reposition to draw iron bars

    def reposition_2():
        pu()
        forward(8.8)
        left(62.5)
        circle(80, 20)
        setheading(180)
        pd()

    reposition_2()
    
    #draws the iron bar which holds the keg together
    
    def ironbar():
        pencolor("dim grey")
        width(7.5)
        forward(77.6)
        backward(77.6)

    ironbar()

    #repositions to draw another iron bar
    def reposition_3():
        pu()
        setheading(0)
        left(75)  
        circle(80, 30)
        setheading(180)
        pd()

    reposition_3()
    #draws second ironbar
    ironbar()

    #repositions turtle to draw label
    def reposition_4():
        pu()
        forward(40)
        left(90)
        forward(12)
        pd()

    reposition_4()

    #draws the label of the gunpowder keg "XXX"
    def label():
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

    label()

#-------------------------------END OF GUNPOWDER KEG ICON----------------------------

#-------------------------BEGINNING OF SKULL ICON----------------------------

#draws a skull token
def skull():
    
    #reposition to draw skull
    def reposition():
        setheading(0)
        pu()
        forward(25)
        left(90)
        forward(20)
        pd()
    reposition()
    
    #draw crossed bones behind skullhead
    def bones():
        pd()
        width(1)
        color("black")
        fillcolor("white")
        setheading(45)
        x = 0
        
        for bone in range(4):
            begin_fill()
            forward(75)
            right(90)
            circle(5, 270)
            right(180)
            circle(5, 270)
            right(90)
            end_fill() 
        
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
    
    
    #reposition to draw skull head
    def reposition():
        pu()
        setheading(135)
        forward(25)
        left(135)
        pd()
        
    reposition()
    
    #draws a skull shape
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
    
    #draw teeth on the skull
    def teeth():
        for teeth in range(4):
            forward(5)
            right(90)
            forward(5)
            backward(5)
            left(90)    
        
    teeth()
    
    #reposition and draw eyes on skull head
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

#-------------------------------END OF SKULL ICON----------------------------

#-------------------------BEGINNING OF RUM ICON----------------------------

#draws a bottle of rum
def rum():
    #repositions to draw rum bottle
    def reposition():
        setheading(0)
        pu()
        forward(30)
        left(90)
        forward(1)
        right(90)
        pd()
        
    reposition()
    
    color("#222334")
    width(2)
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
    
    #draws base bottle and fills
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
                 ['forward', 6, 90],
                 ['forward', 11.5, 90],
                 ['forward', 6, 270],
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

    def label():
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

    label()
    
    #reposition to draw RUM text
    commands_5 = [['goto', -23, 90],
                  ['goto', -3.8, 270],
                  ['goto', 4, 0]
                  ]
    setheading(90)
    decoder(commands_5)

    #draw rum text
    pd()
    write("RUM", font=("Arial", 12, "normal"))

    
#-------------------------------END OF RUM ICON----------------------------



#main function which takes random path + follows instructions given
def follow_path(replaceme):
    speed("fastest")
    import random
    #take the value from the randomly selected path and draw that specific token
    #once drawn the function will choose a random pirate saying and print it with the item found
    def token_draw(token_num):
        pirate_saying = ["Aargh!",
                         "Shiver Me Timbers!",
                         "Avast Ye!",
                         "Blimey!",
                         "Ahoy Matey!",
                         "Thar she blows!",
                         "Yo Ho Ho!"]
        pd()
        if token_num == 0:
            chest()
            print(random.choice(pirate_saying), "You Found A Chest!")
        elif token_num == 1:
            bomb()
            print(random.choice(pirate_saying), "You Found A Bomb!")
        elif token_num == 2:
            gunpowder()
            print(random.choice(pirate_saying), "You Found A Gunpowder Keg!")
        elif token_num == 3:
            skull()
            print(random.choice(pirate_saying), "You Found A Skull!")
        elif token_num == 4:
            rum()
            print(random.choice(pirate_saying), "You Found A Bottle O' Rum!")
        else:
            print("Token Number Not Understood")

    #move to whichever start position is chosen
    def start_pos(start):
        pu()
        if start == "Top left":
            goto(0,600)
        elif start == "Top right":
            goto(600,600)
        elif start == "Centre":
            goto(300,300)
        elif start == "Bottom left":
            goto(0,0)
        elif start == "Bottom right":
            goto(600,0)
        else:
            print("Starting Instruction Not Understood!")
        pd()

    #draws the legend
    def draw_legend():
        pu()
        goto(750, 700)
        pd()
        fillcolor("white")
        begin_fill()
        for legend_container in range(2):
            forward(300)
            right(90)
            forward(700)
            right(90)
        end_fill()
        pu()
        forward(30)
        right(90)
        forward(100)
        left(90)
        pd()
        write("LEGEND", font=("Arial", 30, "normal"))

        l = 0
        legend_text = ["Chest",
                       "Bomb",
                       "Gunpowder Keg",
                       "Skull",
                       "Bottle O' Rum"]
        for legend_items in legend_text:
            pu()
            setheading(270)
            forward(100)
            left(90)
            pd()
            start_coord = pos()
            
        
            if l == 0:
                chest()
            elif l == 1:
                bomb()
            elif l == 2:
                gunpowder()
            elif l == 3:
                skull()
            elif l == 4:
                rum()

            pu()   
            goto(start_coord)
            setheading(0)
            forward(110)
            left(90)
            forward(30)
            right(90)
            color("black")
            pd()
            write(legend_text[l], font=("Arial", 12, "normal"))
            pu()
            goto(start_coord)
            pd()
            l += 1
  
    draw_legend()
    #sets up turtle ready to draw treasure map tokens and defines empty lists
    pu()
    goto(0,0)
    pd()
    coords = []
    token_num_count = []
    
    
    
    #start decoding the instructions
    for instruction in replaceme:
        direction = instruction[0]
        number_of_squares = instruction[1]
        token_num = instruction[2]
        token_num_count.append(token_num)
        coord = pos()
        x = coord[0]
        y = coord[1]

        #choose where to start     
        if direction == "Start":
            start_pos(number_of_squares)
            start_coord = pos()
            token_draw(token_num)
            pu()
            goto(start_coord)
            pd()
        #choose which direction to go and move in that direction a number of times
        elif direction == "North":
            pu()
            setheading(90)
            forward(number_of_squares*100)
            pd()
            start_coord = pos()
            token_draw(token_num)
            pu()
            goto(start_coord)
            pd()
                    
        elif direction == "East":
            pu()
            setheading(0)
            forward(number_of_squares*100)
            pd()
            start_coord = pos()
            token_draw(token_num)
            pu()
            goto(start_coord)
            pd()
            
        elif direction == "South":
            pu()
            setheading(270)
            forward(number_of_squares*100)
            pd()
            start_coord = pos()
            token_draw(token_num)
            pu()
            goto(start_coord)
            pd()
            
        elif direction == "West":
            pu()
            setheading(180)
            forward(number_of_squares*100)
            pd()
            start_coord = pos()
            token_draw(token_num)
            pu()
            goto(start_coord)
            pd()
        else:
            print("This Instruction Is Not Understood!")
            
        print(" ")
        coords.append(start_coord)

    def token_counter(token_num_count):
        token_totals = []
        y = 0
        for token in range(5):
            token_totals.append(token_num_count.count(y))
            y += 1   
        text_coords = [[890.00,530.00],
                       [890.00,430.00],
                       [890.00,330.00],
                       [890.00,230.00],
                       [890.00,130.00]]

        legend_text = ["Chest =",
                       "Bomb =",
                       "Gunpowder Keg =",
                       "Skull =",
                       "Bottle O' Rum ="]
        token_count = len(token_num_count)
        x = 0
        color("black")
        for item in token_totals:
            pu()
            goto(text_coords[x])
            pd()
            output_1 = legend_text[x] + " " + str(token_totals[x])
            write(output_1, font=("Arial", 12, "normal"))
            x += 1
        pu()
        goto(800, 50)
        pd()
        setheading(0)
        output_2 = "You found" + " " + str(token_count) + " " + "tokens!"
        write(output_2, font=("Arial", 16, "normal"))
        
    token_counter(token_num_count)      

#
#--------------------------------------------------------------------#



#-----Main Program---------------------------------------------------#
#
# This main program sets up the background, ready for you to start
# drawing your solution.  Do not change any of this code except
# as indicated by the comments marked '*****'.
#

# Set up the drawing canvas
create_drawing_canvas()

# Control the drawing speed
# ***** Modify the following argument if you want to adjust
# ***** the drawing speed
speed('fastest')

# Decide whether or not to show the drawing being done step-by-step
# ***** Set the following argument to False if you don't want to wait
# ***** forever while the cursor moves around the screen
tracer(True)

# Give the drawing canvas a title
# ***** Replace this title with a description of your solution's theme
# ***** and its tokens
title("A pirate map! Try to find all the pirate tokens!")

### Call the student's function to follow the path
### ***** While developing your program you can call the follow_path
### ***** function with one of the "fixed" data sets, but your
### ***** final solution must work with "random_path()" as the
### ***** argument to the follow_path function.  Your program must
### ***** work for any data set that can be returned by the
### ***** random_path function.
#follow_path(fixed_path_5) # <-- used for code development only, not marking
follow_path(random_path()) # <-- used for assessment


# Exit gracefully
# ***** Change the default argument to False if you want the
# ***** cursor (turtle) to remain visible at the end of the
# ***** program as a debugging aid
release_drawing_canvas()

#
#--------------------------------------------------------------------#
