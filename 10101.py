list=[]
for i in range(1,21):
    list=list+[i%2]
print(*list,sep=" ")
list=[]
n=int(input("Enter the total number of 1's and 0's: "))
for i in range(1,n+1):
    list=list+[i%2]
print(*list,sep=" ")
