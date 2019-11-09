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
    # Set the repeat flag to True
    do_again = True

    while do_again == True:
        # Get a number of feet from the user and then pass the input to the
        #   feet_to_inches function.
        feet = float(input('Enter the number of feet: '))
        inches = feet_to_inches(feet)

        # Print the result to the screen.
        print(f'{feet} feet = {inches} inches')

        # Check whether or not the program should run again.
        ask_ok()

# Define the feet_to_inches function.
def feet_to_inches(feet):
    # Accepts feet and multiplies it by 12 to convert it to inches. Then
    #  returns the number of inches.
    inches = feet * INCHES_PER_FOOT
    return inches

# Define the ask_ok function
def ask_ok(prompt, retries=4, reminder='Please answer y/n.'):
    # Asks the user if they would like to run the program again, and returns
    #   False if they do not.
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

# Call the main function to exeute the program.
main()
