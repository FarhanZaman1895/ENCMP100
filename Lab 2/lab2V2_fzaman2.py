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

    # Rule 2, test if the sum is even
    if code.sum()%2 == 1:

        # Arrays used for rules 3 and 4
        POSSIBLE_DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] # Days
        POSSIBLE_LOCATIONS = ["bridge", "library", "river crossing", "airport", "bus terminal", "hospital", "railway station"] # Places
        VALID_RANGE = np.arange(1, 8) # Range of values allowed for day and place

        # Rule 3, calculate the day of the rescure

        # Find the day value and test if it is real
        day = (code[2] * code[1]) - code[0]

        if day in VALID_RANGE:
            # Assigns the rescue day
            rescueDay = POSSIBLE_DAYS[day - 1]

            # Rule 4, calculate the location of the rescue 

            # Find the place value
            placeCalc = code[2] ** code[1]
            if placeCalc%3 == 0:
                place = code[5] - code[4]
            else:
                place = code[4] - code[5] 

            # Test if the place is valid
            if place in VALID_RANGE:

                # Assigns the rescue location
                rescuePlace = POSSIBLE_LOCATIONS[place - 1]
                print("Rescued on " + rescueDay + " at the " + rescuePlace + ".")

            else: # Prints error message for the if statements 
                print("Decoy message: Invalid rendezvous point.")

        else:
            print("Decoy message: Invalid rescue day.")

    else: 
        print("Decoy message: Sum is even.")
else:
    print("Decoy message: Not a nine-digit number.")
