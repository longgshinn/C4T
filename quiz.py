question_pack=[
    {
        "question":"1+1=?",
        "choices":["A.0","B.1","C.2","D.3"],
        "rightchoice":"C"
    },
    {
        "question":"2+7=?",
        "choices":["A.4","B.9","C.2","D.11"],
        "rightchoice":"B"
    },
    {
        "question":"5:2=?",
        "choices":["A.2","B.5","C.3","D.2.5"],
        "rightchoice":"D"
    }
]
causai=[]
correct_answer_count=0
for i in range(len(question_pack)):
    print("Cau hoi",i+1,":")
    print()
    print(question_pack[i]["question"])
    print()
    print(*question_pack[i]["choices"],sep="\n")
    print()
    user_choice=input("M chon dap an gi?").upper()
    print()
    if user_choice==question_pack[i]["rightchoice"]:
        print("ghe vay")
        correct_answer_count+=1
    else:
        print("ngu")
        causai.append(i+1)
    print()
print("Result: ")
print("{0} correct answers".format(correct_answer_count))
print("{0}%".format(round(correct_answer_count/len(question_pack)*100,2)))
print("M sai o cau: "),
print(*causai,sep=", ")