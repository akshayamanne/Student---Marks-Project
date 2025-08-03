name=input("enter your name:")
total=0
marks_list=[]
for i in range (5):
    marks=int(input("subject"+str(i+1) + ":"))
    marks_list.append(marks)
    total=sum(marks_list)
    average=total/5
print("the total is:",total)
print("the average is:",average)
if average >= 50:
    print("you passed")
else:
    print("you failed.")