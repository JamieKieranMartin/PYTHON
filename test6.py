from turtle import *

setup(800, 800)

data_set = [[5, -50, 'red'],
            [-100, 10, 'blue'],
            [-200, 200, 'green'],
            [-150, -100, 'yellow']
            ]

for data in data_set:
    penup()
    goto(data[1], data[0])
    color(data[2])
    pensize(abs(data[1])/10)
    dot()
    
