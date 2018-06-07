list=[]
for i in range(20):
    list=list+[i]
print(*list,sep=" ")
list=[]
n=int(input("Enter a number: "))
for i in range(n):
    list=list+[i]
print(*list,sep=" ")
