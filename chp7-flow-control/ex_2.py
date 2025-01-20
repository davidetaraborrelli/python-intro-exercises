# Exercise 2
# Write a function, even_or_odd, that determines whether its argument is an even or odd number. If it's even, the function should print 'even'; otherwise, it should print 'odd'. Assume the argument is always an integer.

def even_or_odd(number):
    if number % 2 == 0:
        return "even"
    else:  
        return "odd"

def get_number():
    return int(input("Enter a number: "))

number = get_number()
print(f"The number {number} is {even_or_odd(number)}.")