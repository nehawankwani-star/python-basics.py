# Simple Calculator

def calculator():
    print("=== Simple Python Calculator ===")
    print("Operations: +, -, *, /")

    while True:
        try:
            num1 = float(input("\nEnter first number: "))
            operator = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:
                    print("Error: Cannot divide by zero.")
                    continue
                result = num1 / num2
            else:
                print("Invalid operation.")
                continue

            print(f"Result: {result}")

            again = input("\nDo you want to calculate again? (yes/no): ")
            if again.lower() != "yes":
                print("Thanks for using the calculator!")
                break

        except ValueError:
            print("Please enter valid numbers.")


calculator()

# Student Grade Calculator

print("=== Student Grade Calculator ===")

name = input("Enter student name: ")

math = float(input("Enter Math marks: "))
english = float(input("Enter English marks: "))
science = float(input("Enter Science marks: "))

total = math + english + science
average = total / 3

if average >= 90:
    grade = "A+"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print("\n=== Student Result ===")
print("Student Name:", name)
print("Total Marks:", total, "/ 300")
print("Average:", round(average, 2))
print("Grade:", grade)

if grade == "F":
    print("Status: Fail")
else:
    print("Status: Pass")
import random

print("=== Number Guessing Game ===")
print("I have chosen a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    try:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("\nCongratulations! You guessed the number!")
            print("The number was:", secret_number)
            print("Number of attempts:", attempts)
            break

    except ValueError:
        print("Please enter a valid number.")

        
    import random
import string

print("=== Password Generator ===")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("\nGenerated Password:", password)

# Simple Expense Tracker

expenses = []

print("=== Expense Tracker ===")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. View Total")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))

        expenses.append({
            "name": name,
            "amount": amount
        })

        print("Expense added successfully!")

    elif choice == "2":
        if len(expenses) == 0:
            print("No expenses recorded.")
        else:
            print("\n=== Your Expenses ===")

            for expense in expenses:
                print(f"{expense['name']}: ${expense['amount']:.2f}")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"\nTotal Expenses: ${total:.2f}")

    elif choice == "4":
        print("Thank you for using the Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
