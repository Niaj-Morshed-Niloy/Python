#write a program to find out whether a given post is talking about "Anon" or not.

post=input("Enter the post: ")

if("anon" in post.lower()):
    print("This post is talking about Anon")
else:
    print("This post is not talking about Anon")