#ASSIGNMENT: Conditional Statements And Functions

# Assignment: Conditional Statements
# Q:2
x = 15 
if x > 20:
    print('A')
elif x > 10:
    print('B')
else:
    print('C')

# AND Operator Example

# Q:3 This question indicates that both conditions must be true.

# example:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Q:4
age = 17
has_id = True
if age >= 18 and has_id: 
    print('Allowed') 
else: 
    print('Denied')

# Assignment: Functions

# Q:7
def calculate(a, b):
    return a + b 

print(calculate(5, 3))

# Q:9
def greet(name='Student'): 
    print('Hello', name)

greet()

# Conditional Statements and Functions

# Q:10
def check_number(num): 
    if num % 2 == 0:
        return 'Even'
    else:
        return 'Odd'

print(check_number(7))