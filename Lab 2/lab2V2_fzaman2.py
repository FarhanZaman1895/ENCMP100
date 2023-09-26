# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Farhan Zaman
# Student CCID: fzaman2
# Others: 
# Jason Wang (1%)
# Farhan Zaman (99%)
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
import numpy as np

print('Lab 2 - Version 1')
code = input('Please enter a code to break: ')
code = np.array(list(code),dtype=int)

# Rule 1, test if the length of the number is 9
if len(code) == 9:

    # Rule 2, test if the sum is even
    if code.sum()%2 == 1:

        # Rule 3
        day = (code[2] * code[1]) - code[0]
        validDayRange = np.arange(1, 8)
        if day in validDayRange:
            print("Day = %d" % day)

        # Rule 4
        placeCalc = code[2] ** code[1]
        if placeCalc%3 == 0:
            place = code[5] - code[4]
        else:
            place = code[4] - code[5] 
        print("Place = %d" % place)
    else:
        print("Decoy message: Sum is even")
else:
    print("Decoy message: Not a nine-digit number")
