words=["Donkey","bad","ganda"]

with open("Dfile.txt","r") as f:
    content=f.read()

for word in words:
    content= content.replace(word, "#"*len(word))

with open("Dfile.txt","w")as f:
    f.write(content)
