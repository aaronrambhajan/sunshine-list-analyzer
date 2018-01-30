import functions

print('This program calculates the average salary increase of all UofT \
employees on the Sunshine List who were employed between two given years, \
ranging 2006 to 2016. The Sunshine List includes public sector employees \
with salaries in excess of $100k.')

answer = 'yes'

while answer.lower() == 'yes' or answer.lower() == 'yeah' \
      or answer.lower() == 'ye' or answer.lower() == 'y' \
      or answer.lower() == 'ya':

# Prompt for first input.
    one = input('\nEnter the starting year: ')

# Checks that input is numeric.
    while one.isnumeric() == False:
        one = input('Year information must be a number between 2006 and \
2016, please! Enter the starting year: ')

# Checks that input is within valid year range.
    while int(one) < 2006 or int(one) > 2016:
        one = int(input('Year information must be between 2006 and 2016, \
please! Re-enter the starting year: '))

# Prompt for second input.
    two = input('\nEnter the ending year: ')
    
# Checks that input is numeric.
    while two.isnumeric() == False:
        two = input('Year information must be a number between 2006 and \
2016, please! Enter the ending year: ')

# Checks that input is within valid year range.
    while int(two) < 2006 or int(two) > 2016 or int(one) == int(two):
        two = int(input('Year information must be between 2006 and 2016, \
please! Re-enter the ending year: '))
        
# Run program according to input.
    functions.main_program(one, two)

# Reprompt, and conclude.
    answer = input('\nAny more requests? ')

print("\nHope you found what you're looking for! Developed in 2017 by Aaron \
Rambhajan.\n")
