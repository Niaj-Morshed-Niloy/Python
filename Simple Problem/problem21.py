#Write a python program to find the greatest of four numbers entered by the user.

a1=int(input())
a2=int(input())
a3=int(input())
a4=int(input())

if(a1>a2 and a1>a3 and a1>a4):
    print("Greatest number:",a1)
if(a2>a1 and a2>a3 and a2>a4):
    print("Greatest number:",a2)
if(a3>a1 and a3>a2 and a3>a4):
    print("Greatest number:",a3)
# if(a1>a2 and a1>a3 and a1>a4):
#     print("Greatest number:",a1)
else:
    print("greatest number:",a4)