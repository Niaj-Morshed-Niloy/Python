#Create an empty dictionary. Allow 4 friends to enter their favorite language as value and use key as their names. Assumes that the names are unique.

dic={}
name=input("Enter friends name: ")
lang=input("Enter language name: ")
dic.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
dic.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
dic.update({name:lang})

name=input("Enter friends name: ")
lang=input("Enter language name: ")
dic.update({name:lang})

print(dic)
