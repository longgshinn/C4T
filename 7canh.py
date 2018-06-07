from turtle import *
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
speed(0)
for i in range (3,8):
    pencolor(colors[(i-3)%5])
    for _ in range(i):
        forward(100)
        left(360/i)
mainloop()