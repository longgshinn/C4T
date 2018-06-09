numbers=[1,2,23,1,34,5,4,6,7,9,34,6,4,3,8]
count=0
number=int(input("Enter a number? "))
if number in numbers:
    for i in range(len(numbers)):
        if numbers[i]==number:
            count+=1
print("{0} appears {1} times in my list".format(number,count))