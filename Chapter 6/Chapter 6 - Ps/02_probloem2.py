# Write a program to find out wheather a student has passed or failed if it requires a total of 40% and at least 33% in each sunject to pass. Assume 3 subjects and take marks as an input from the user

mark1 = int(input("Enter marks for first subject: "))
mark2 = int(input("Enter marks for second subject: "))
mark3 = int(input("Enter marks for third subject: "))

# Check for total percentage
total_percentage = (100*(mark1 + mark2 + mark3))/300

if(total_percentage>40 and mark1>=33 and mark2>=33 and mark3>=33):
    print("You are Passed!", total_percentage)
else:
    print("You are failed!", total_percentage)