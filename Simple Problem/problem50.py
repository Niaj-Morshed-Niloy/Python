#write a program to make a copy of a text file.

with open("file.txt")as f:
    content= f.read()
with open("file_copy.txt","w")as f:
    f.write(content)
    