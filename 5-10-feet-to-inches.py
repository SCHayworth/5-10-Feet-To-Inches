# 5-10 Feet to Inches
# Shaun Hayworth
# CIS 2
# 11-09-2019
# Source code and revision history available at
#   https://github.com/SCHayworth/5-10-Feet-To-Inches

# Program calculates how many inches are in a given number of feet using a
#   value-returning function, and prints the result to the screen.

# Initialize a constant for the number of inches in one foot
INCHES_PER_FOOT = 12

# Define the main function.
def main():
    # Get a number of feet from the user and then pass the input to the
    #   feet_to_inches function.
    feet = float(input('Enter the number of feet: '))
    inches = feet_to_inches(feet)

    # Print the result to the screen.
    print(f'{feet} feet = {inches} inches')

# Define the feet_to_inches function.
def feet_to_inches(feet):
    # Accepts feet and multiplies it by 12 to convert it to inches. Then
    #  returns the number of inches.
    inches = feet * INCHES_PER_FOOT
    return inches

# Call the main function to exeute the program.
main()
