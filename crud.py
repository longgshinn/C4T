items = ["Our items: T-Shirt","Sweater"]
for i in range(4):
    action = input("welcome to our shop, what do you want (C, R, U, D)? ").upper()
    if action == "R":
        print(*items,sep = ", ")
    elif action == "C":
        newitem = input("Enter new item: ")
        items.append(newitem)
        print(*items, sep = ", ")
    elif action == "U":
        pos = int(input("Update position?"))
        newitem = input("New item?")
        items.pop(pos-1)
        items.insert(pos-1,newitem)
        if pos==1:
            items[0]="Our items: "+items[0]
        print(*items, sep=", ")
    elif action == "D":
        deletepos = int(input("Delete position?"))
        items.pop(deletepos-1)
        if deletepos==1:
            items[0]="Our items: "+items[0]
        print(*items, sep=", ")
