# Wite a program to greet all the person name stored in a list 'l' and which starts with S. l = ["Mohan", "Soham", "Sachin", "Rahul"]

l = ["Mohan", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith("S")):
        print(f"Hello {name}")