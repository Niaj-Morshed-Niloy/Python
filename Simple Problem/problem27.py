# write a program to print multiplication table of a given number using the loop.

n=int(input("Enter a number:"))

for i in range(1,11):
    print(f"{n} X {i} ={n*i}")
