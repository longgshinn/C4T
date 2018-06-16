import math
def sincos(x):
    y=[]
    z=[]
    tong_z=0
    for i in range(len(x)):
        y.append(math.pi/2-x[i])
        z.append(math.cos(x[i])-math.sin(x[i]))
    for i in range(len(z)):
        tong_z+=z[i]
    print("y =",y)
    print("z =",z)
    print("Tong cac phan tu cua z la:",tong_z)