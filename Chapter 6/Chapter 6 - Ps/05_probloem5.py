# Write a program which finds out wheather a given name is present in a list or not.

l = ["Mohan", "Gotya", "Hiraman", "Peter"]

name = input("Enter your name: ")

if(name in l):
    print("Name is in the list")
else:
    print("Name is not in the list")