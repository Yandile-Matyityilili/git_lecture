# Question 1: Arithmetic and Assignment Operators 
x = 17
y = 1
# TODO: Add 3 to x using the += operator
x += 3 
# TODO: Multiply y by 2 using the *= operator
y *= 2
# TODO: Divide x by y and store the result in a variable called 'result'
result=(x / y)
# TODO: Print the value of 'result'
print(result)
#------------------------------------------------------------------------------------
# Question 2: Comparison and Logical Operators
a = 5
b = 3
c = 2
# TODO: Create a condition that checks if a is greater than b
if a > b:
   print("a is greater than b")

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b % 3 == 0:
    print("b is even")
else:
   print("b is odd")
# TODO: Create a condition that checks if c is less than or equal to a
if c <= a:
   print("c is less than a")
else :
   print("c is greater than a")
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a
final_conditions = a > b or (a % b or c <= a)

if final_conditions:
    print(f"a is greater than b, b is even, c is less than or equal to a: {final_conditions}")
else:
   print("final conditions not true")

# TODO: Print the value of 'final_condition'

#------------------------------------------------------------------------------------
# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score=int(input("Enter test score (0-100)"))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
test_score = (0-100)

if score in range(90,101):
    print("A")
elif score in range(80,90):
    print("B")
elif score in range(70,80):
    print("C")
elif score in range(60,70):
    print("D")
else:
    print("F")
  
# TODO: Print the grade for the given score

#------------------------------------------------------------------------------------
# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'
num1=int(input("Enter the first number"))
num2=int(input("Enter the second number"))
# TODO: Ask the user to input an operation (+, -, *, /) and store it in a variable called 'operation'
operation = input("Enter an operation")
# TODO: Handle the case of division by zero

if num2 ==0:
    results ="Cannot divide by zero"
# TODO: Use conditional statements to perform the chosen operation on num1 and num2
elif operation == '+':
    results = num1 + num2
elif operation == '-':
    results = num1 - num2
elif operation == '*':
    results = num1 * num2
elif operation == '/':
    results = num1 / num2
# TODO: Print the result of the operation 
print(f"{results}") 