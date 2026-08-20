# 1. Variables
name = "Ali"
age = 20
print(name, age)

# 2. Lists
fruits = ["Apple", "Banana", "Mango"]
print(fruits[0])

# 3. Loops
for fruit in fruits:
    print(fruit)

# 4. Functions
def greet(name):
    return "Hello " + name

print(greet("Ali"))
# Beginner-Friendly Python Program

# Function to greet the user
def greet(name):
    print("\nHello", name, "! Welcome to Python.")

# Get user information
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# Variables
print("\nYour name is:", name)
print("Your age is:", age)

# Check age
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# List of favorite subjects
subjects = ["Python", "AI", "Machine Learning"]

print("\nYour subjects:")
for subject in subjects:
    print("-", subject)

# Simple calculator
num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

print("\nCalculator:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero.")

# Call the function
greet(name)

print("\nProgram completed successfully!")
