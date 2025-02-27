
print("Hello, I am a program to calculate the average value.")
user_input = input("Please enter the number you need (end with '!'): ")
add = 0  # Used to accumulate all input numbers
i = 0    # Used to record the number of digits entered
warehouse = []  # Used to store all numbers entered by the user

# Use the while loop to process user input
while user_input != "!":
    try:
        number = int(user_input)  # Convert input to integer
        add =add+ number  # Add to total
        warehouse.append(number)  # Store numbers in a list
        i = i + 1  # Counter plus 1
    except ValueError:
        print("Invalid input. Please enter a valid integer.")  # If the format is wrong, let him enter an integer
    user_input = input("Please enter the number you need (end with '!'): ")

# Prevent divide by zero errors
if i > 0:
    average = add / i
    print("The average value is: " + str(average))
    print("You entered the following numbers: " + str(warehouse))
else:
    print("No valid numbers were entered.")