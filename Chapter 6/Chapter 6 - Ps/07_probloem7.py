# Write a program to find out weather a given post is talking about "Mohan" or not.

post = input("Enter your post: ")

if("Mohan".lower() in post.lower()):
    print("This post is talking about Mohan")
else:
    print("This post is not talking about Mohan")