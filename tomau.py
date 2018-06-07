from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(0)
for i in range (5):
    pencolor(colors[i%5])
    fillcolor(colors[i%5])
    begin_fill()
    for _ in range(2):
        forward(50)
        left(90)
        forward(100)
        left(90)
    end_fill()
    forward(50)
mainloop()