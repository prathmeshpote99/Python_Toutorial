# Write a program to calculate the factorial of a given number using for loop
# Ex: 5! = 1 * 2 * 3 * 4 * 5

n = int(input("Enter the number: "))

product = 1
for i in range (1, n+1):
    product = product * i
    
print(f"The factorial of {n} is {product}")