# 5-10 Feet to Inches
# Shaun Hayworth
# CIS 2
# 11-09-2019
# Source code and revision history available at
#   https://github.com/SCHayworth/5-10-Feet-To-Inches

# Program calculates how many inches are in a given number of feet using a
#   value-returning function, and prints the result to the screen.

# Define the main function
def main():
    # Get a number of feet from the user and then pass the input to the
    #   feet_to_inches function.
    feet = float(input('Enter the number of feet: '))
    inches = feet_to_inches(feet)

    # Print the result to the screen.
    print(f'{feet} = {inches} inches')

    
