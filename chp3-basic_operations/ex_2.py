# Use the REPL and the arithmetic operators
# to extract the individual digits of 4936:
number = 4936
print(f'One place is {number % 10}')
print(f'Ten place is {number // 10 % 10}')
print(f'Hundreds place is {number // 100 % 10}')
print(f'Thousands place is {number // 1000 % 10}')