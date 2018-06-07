import random
wordlist=["champion","league","legend","football"]
word1=["c","h","a","m","p","i","o","n"]
word2=["l","e","a","g","u","e"]
word3=["l","e","g","e","n","d"]
word4=["f","o","o","t","b","a","l","l"]
randnum=random.randint(1,4)
if randnum==1:
    for i in range(10):
        m=random.randint(0,7)
        n=random.randint(0,7)
        x=word1[m]
        word1[m]=word1[n]
        word1[n]=x
    print(*word1,sep=" ")
    answer=str.lower(input("Your answer: "))
    if answer=="champion":
        print("Hura")
    else:
        print(":(")
if randnum==2:
    for i in range(10):
        m = random.randint(0,5)
        n = random.randint(0,5)
        x = word2[m]
        word2[m] = word2[n]
        word2[n] = x
    print(*word2, sep=" ")
    answer = str.lower(input("Your answer: "))
    if answer == "league":
        print("Hura")
    else:
        print(":(")
if randnum==3:
    for i in range(10):
        m = random.randint(0,5)
        n = random.randint(0,5)
        x = word3[m]
        word3[m] = word3[n]
        word3[n] = x
    print(*word1, sep=" ")
    answer = str.lower(input("Your answer: "))
    if answer == "legend":
        print("Hura")
    else:
        print(":(")
if randnum==4:
    for i in range(10):
        m = random.randint(0,7)
        n = random.randint(0,7)
        x = word4[m]
        word4[m] = word4[n]
        word4[n] = x
    print(*word4, sep=" ")
    answer = str.lower(input("Your answer: "))
    if answer == "football":
        print("Hura")
    else:
        print(":(")


