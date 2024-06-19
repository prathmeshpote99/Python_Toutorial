# Write a program to find wheather a given username contains less than 10 characters or not

a = input("Enter your username: ")

if(len(a)<10):
    print("Username must be 10 characters")
else:
    print("Username is valid")