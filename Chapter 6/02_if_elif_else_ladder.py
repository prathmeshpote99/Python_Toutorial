a = int(input("Enter your age: "))

# if elif else ladder

if (a>=18):
    print("You are above the age of consent")
    print("Good for you")
elif(a<0):
    print("Your are entering negative age")
elif(a==0):
    print("Your are entering 0 age which is not valid")
else:
    print("You are below the age of consent")
    print("Sorry kiddo")