map={
    "size_x":5,
    "size_y":5,
}
player={
    "x":3,
    "y":3
}
boxes=[
    {"x":1,"y":2},
    {"x":2,"y":3},
    {"x":3,"y":2},
]
destinations=[
    {"x":4,"y":2},
    {"x":1,"y":3},
    {"x":1,"y":1},
]
dangerous=[
    {"x":0,"y":3},
    {"x":2,"y":1}
]
while True:
    for y in range(map["size_y"]):
        for x in range(map["size_x"]):
            player_is_here=False
            box_is_here=False
            des_is_here=False
            danger_is_here=False
            for box in boxes:
                if box["x"]==x and box["y"]==y:
                    box_is_here=True
                    break
            for des in destinations:
                if des["x"]==x and des["y"]==y:
                    des_is_here=True
                    break
            for danger in dangerous:
                if danger["x"]==x and danger["y"]==y:
                    danger_is_here=True
                    break
            if x==player["x"] and y==player["y"]:
                player_is_here=True
            if player_is_here:
                print("P ",end="")
            elif box_is_here:
                print("B ",end="")
            elif des_is_here:
                print("D ",end="")
            elif danger_is_here:
                print("X ",end="")
            else:
                print("- ",end="")
        print()
    win=True
    for box in boxes:
        if box not in destinations:
            win=False
    if win:
        print("You win!!!")
        break
    move=input("Your move: ").lower()
    dx=0
    dy=0
    if move =="w":
        dy=-1
    elif move=="s":
        dy= 1
    elif move =="a":
        dx=- 1
    elif move=="d":
        dx= 1
    else:
        print("dbt choi a")
        print("di lai mm di")
    if (0<=player["x"]+dx<=map["size_x"]-1) and (0<=player["y"]+dy<=map["size_y"]-1):
        player["x"]+= dx
        player["y"]+= dy
    for box in boxes:
        if player["x"]==box["x"] and player["y"]==box["y"] and (0 <= box["x"] + dx <= map["size_x"] - 1) and (0 <= box["y"] + dy <= map["size_y"] - 1):
            box["x"]+=dx
            box["y"]+=dy
    for danger in dangerous:
        if player["x"]==danger["x"] and player["y"]==danger["y"]:
            player["x"]-=dx
            player["y"]-=dy
    for danger in dangerous:
        for box in boxes:
            if box["x"]==danger["x"] and box["y"]==danger["y"]:
                player["x"]-=dx
                player["y"]-=dy
                box["x"]-=dx
                box["y"]-=dy
    for i in range(len(boxes)):
        if (boxes[i]["x"]==boxes[i-1]["x"] and boxes[i]["y"]==boxes[i-1]["y"])\
                or (boxes[i]["x"]==boxes[i-2]["x"] and boxes[i]["y"]==boxes[i-2]["y"]):
            boxes[i]["x"]-=dx
            boxes[i]["y"]-=dy
    for box in boxes:
        if player["x"]==box["x"] and player["y"]==box["y"] :
            player["x"]-=dx
            player["y"]-=dy