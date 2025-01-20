# EXERCISE 3
#  Write a program that uses a multiply function 
# to multiply two numbers and returns the result. 
# Ask the user to enter the two numbers, 
# then output the numbers and result as a simple equation.

# $ python multiply.py
# Enter the first number: 3.1416
# Enter the second number: 2.7183
# 3.1416 * 2.7183 = 8.53981128

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))
def multiplicator(x, y):
    return x * y
multiplicator(x, y)
print(f"{x} * {y} = {multiplicator(x, y)}")

# second version with getter function

def multiply(x, y):
    return x * y

def get_numbers(prompt):
    input = input(prompt)
    return float(input)

fist_number = get_numbers("Enter the first number: ")
second_number = get_numbers("Enter the second number: ")

product = multiply(fist_number, second_number)

print(f"{fist_number} * {second_number} = {product}")