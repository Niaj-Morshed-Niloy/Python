#write a program to calculate the grade of a stufent from his marks from the following scheme:

marks=int(input("Enter the marks:"))

if(marks<=100 and marks>=90):
    print("Ex")
elif(marks<90 and marks>=80):
    print("A")
elif(marks<80 and marks>=70):
    print("B")
elif(marks<70 and marks>=60):
    print("C")
elif(marks<60 and marks>=50):
    print("D")
elif(marks<50):
    print("F") 