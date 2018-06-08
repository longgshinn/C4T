flock=[5,7,300,90,24,50,75]
print("Hello, my name is Hiep and these are my sheep size")
print(flock)
for x in range(3):
    biggest=flock[1]
    for i in range(7):
        if flock[i]>biggest:
            biggest=flock[i]
    print("Now my biggest sheep has size",biggest,"let's shear it")
    for i in range(7):
        if flock[i]==biggest:
            flock[i]=8
    print("After shearing, here is my flock ")
    print(flock)
    for i in range(7):
        flock[i]+=50
    print(" ")
    print("MONTH",x+1)
    print("One month has passed, now here is my flock")
    print(flock)
total=0
for i in range(7):
    total+=flock[i]
money=str(total*3)+"$"
print("My flock has size in total:",total)
print("I would get",total,"* 3$ =",money)
