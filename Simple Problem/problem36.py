#write a program using functions to find greatest three numbers.

def anon():
    a=int(input("Enter number:"))
    b=int(input("Enter number:"))
    c=int(input("Enter number:"))

    if(a>b and a>c):
        print("Greatest number is a")
    elif(b>a and b>c):
        print("Greatest number is b")
    else:
        print("Greatest number is C")


anon()
print("Done")
    



"""
def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>b and c>a):
        return c

a=2
b=6
c=111
print(greatest(a,b,c))

"""