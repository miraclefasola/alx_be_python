# pattern_drawing.py

# Prompt the user for the pattern size
user_input = int(input("Enter the size of the pattern: "))


row = 0
# Use a while loop to handle the rows
while row < user_input:
    # Use a for loop to print asterisks in each row
    for col in range(user_input):
        print("*", end="")  # Print without newline
    print()  # Move to the next line after each row
    row += 1