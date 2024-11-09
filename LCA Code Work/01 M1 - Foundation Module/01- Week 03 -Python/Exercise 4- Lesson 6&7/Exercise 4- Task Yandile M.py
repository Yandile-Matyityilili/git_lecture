# Question 1: Using a for loop with a list
fruits = ["apple","banana","pear","pineapple","watermelon"]
# TODO: Create a list of fruits
for friut in fruits:
    print(friut)
# TODO: Use a for loop to print each fruit in the list
    
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
i = 5
while i>= 1:
    print(i)
    i=i-1

#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
n=1 
while n<= 10:
    print("Square of ",n,"is ",n*n)
    n=n +1
    


#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
list_of_color = ["red" ,"orange" ,"yellow" ,"green" ,"blue" ,"purple" ,"black" ,"white"]
# TODO: Use a for loop to select and print 3 random colors from the list 
for x in range(3):
    colours = random.choice(list_of_color)
    print(colours)
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Division by zero"


# TODO: Import the custom module and use its functions
# Import the custom module
import math_operations as math

# Use a while loop to create a simple calculator
state = True
operation = {
    '+': math.add,
    '-': math.subtract,
    '*': math.multiply,  
    '/': math.divide     
}

while state:
    def cont():
        x = float(input("Enter your first number: "))
        y = float(input("Enter your Second number: "))
        z = input("Choose an operation (+, -, *, /): ")
        if z in operation: 
            return print("Answer:", operation[z](x, y))
        else:
            print("Incorrect operation. Please choose +, -, *, or /.")

    a = input("Do you want to perform a calculation? Yes/No: ").lower()
    if a == "yes":
        cont()
    elif a == "no":
        state = False
        print("Exiting calculator.")
    else:
        print("wrong input")
         
print(math.add(5, 4))
