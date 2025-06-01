# multiplication_table.py

# Prompt the user for a number
number_input = input("Enter a number to see its multiplication table: ")

# Check if the input is a valid number
if number_input.replace('.', '', 1).isdigit():
    number = float(number_input)
    
    # Use a for loop to print the multiplication table from 1 to 10
    for i in range(1, 11):
        result = number * i
        print(f"{number} * {i} = {result}")
else:
    print("Please enter a valid number.")