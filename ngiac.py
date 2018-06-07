from turtle import *
color=['red','blue']
speed(0)
for i in range (3,7):
    pencolor(color[i%2])
    for _ in range(i):
        forward(100)
        left(360/i)
mainloop()