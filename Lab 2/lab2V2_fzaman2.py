# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Farhan Zaman
# Student CCID: fzaman2
# Others: 
# Jason Wang (2%)
# Farhan Zaman (98%)
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions may be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.
#

# Imports
import numpy as np

# Ask the use for the input
print('Lab 2 - Version 1')
code = input('Please enter a code to break: ')
code = np.array(list(code),dtype=int)

# Rule 1, test if the length of the number is 9
if len(code) == 9:

    # Rule 2, test if the sum is even by first using the numpy.sum function to sum the array
    # then, using the modulus operator to find test if the sum is even or od
    if code.sum()%2 == 1:

        # Arrays used for rules 3 and 4
        POSSIBLE_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # Days
        POSSIBLE_LOCATIONS = ["bridge", "library", "river crossing", "airport", "bus terminal", "hospital", "railway station"] # Places
        VALID_RANGE = np.arange(1, 8) # Range of values allowed for day and place

        # Rule 3, calculate the day of the rescue using the given formula, 
        # taking the 3rd digit and multiplying it by the 2nd digit and subtract the 1st digit
        day = (code[2] * code[1]) - code[0]

        # This tests if the day value is valid and would work in
        # the array for the day by testing if it is in the array from 1 to 7 inclusive
        if day in VALID_RANGE:

            # Saves the rescue day for the final print statement
            rescueDay = POSSIBLE_DAYS[day - 1]

            # Rule 4, calculate the location of the rescue, 
            # first by calculating the 3rd digit to the
            # power of the 2nd digit, testing if that is divisible by 3
            # and then either subtracting the 5th value from the 4th
            # or the 4th value from the 5th depending on if it is divisible

            # Find the place value
            placeCalc = code[2] ** code[1]

            # Testing if the calculated value is divisible by 3 by testing if
            # the modulus operator returns a 0 value
            if placeCalc%3 == 0:
                place = code[5] - code[4]
            else:
                place = code[4] - code[5] 

            # Test if the place is valid for the array of locations
            if place in VALID_RANGE:

                # Assigns the rescue location for the final print statement
                rescuePlace = POSSIBLE_LOCATIONS[place - 1]

                # Prints the final rescue day and place if all previous conditions were met
                print("Rescued on " + rescueDay + " at the " + rescuePlace + ".")

            else: # Prints error message for the if statements 
                # Error for rule 4
                print("Decoy message: Invalid rendezvous point.")

        else:
            # Error for rule 3
            print("Decoy message: Invalid rescue day.")

    else: 
        # Error for rule 2
        print("Decoy message: Sum is even.")
else:
    # Error for rule 1
    print("Decoy message: Not a nine-digit number.")
