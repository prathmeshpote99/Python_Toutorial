marks = {
    "Mohan" : 50,
    "Shubham" : 78,
    "Rohan" : 98,
    0: "Soham"
}

print(len(marks))

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Rohan" : 97})
print(marks)