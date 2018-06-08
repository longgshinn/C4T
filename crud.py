action = input("welcome to our shop, what do you want (C,R,U,D) ? ").upper()
items = ["Tshirt","Sweater"]
if action == "R":
    print("Our items : ")
    print(*items,sep = ",")
elif action == "C":
    newitem = input("Enter new item :")
    items.append(newitem)
    print("Our items : ")
    print(*items, sep = ",")
elif action == "U":
    pos = int(input("Update position ?"))
    newitem = input("New item ?")
    items.insert(pos,newitem)
    print("Our items : ")
    print(*items, sep=",")
else:
    deletepos = int(input("Delete position ?"))
    items.pop(deletepos-1)
    print("Our items : ")
    print(*items, sep=",")