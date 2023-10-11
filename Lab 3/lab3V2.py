# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Farhan Zaman
# Student CCID: 1803211
# Others: Jason Wang (2%) Assisted with removing margins from graph
# Farhan Zaman (98%)
# Matplotlib documentation was used to change the increments of the x axis
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
import matplotlib.pyplot as plt
import numpy as np

## CONSTANTS
NUMBER_OF_MONTHS = 12 * 18
START_AMOUNT = 2000
MONTHLY_INTEREST = 0.0625
TUITION_INTEREST = 0.07

# Arrays for tuition interest
artTuit = [5550]
sciTuit = [6150]
engTuit = [6550]

# Variable Monthly Contribution
monthlyContribution = 200

# Initialize y axis for graph
monthlyAmount = [START_AMOUNT]

## CALCULATION

# Saving Calculation
for i in range(1, NUMBER_OF_MONTHS):
    monthlyAmount += [monthlyAmount[i - 1] + (monthlyAmount[i - 1] * (MONTHLY_INTEREST / 12)) + monthlyContribution]

# Tuition Calculation
for i in range(1, 22):
    artTuit += [ artTuit[i-1] * (1 + TUITION_INTEREST) ]
    sciTuit += [ sciTuit[i-1] * (1 + TUITION_INTEREST) ]
    engTuit += [ engTuit[i-1] * (1 + TUITION_INTEREST) ]

totalArtTuit = 0
totalSciTuit = 0
totalEngTuit = 0

for i in range(0, 4):
    totalArtTuit += artTuit[-(i + 1)]
    totalSciTuit += sciTuit[-(i + 1)]
    totalEngTuit += engTuit[-(i + 1)]

## OUTPUTS
print("Version 1 - Solution")
print(f"The savings ammount is {format(monthlyAmount[-1], '.2f')}")
print(f"The cost of the arts program is ${format(totalArtTuit, '.2f')}")
print(f"The cost of the science program is ${format(totalSciTuit, '.2f')}")
print(f"The cost of the engineering program is ${format(totalEngTuit, '.2f')}")

# Make the labels for the ticks along x axis
xTickLabels = np.char.mod("%d", np.arange(0, 19))

# Plot Graph
fig, ax = plt.subplots()
ax.plot(range(0, NUMBER_OF_MONTHS), monthlyAmount, label = "Saving Balance")
ax.hlines(totalArtTuit, 0, NUMBER_OF_MONTHS, color = "orange", label = "Arts")
ax.hlines(totalSciTuit, 0, NUMBER_OF_MONTHS, color = "green", label = "Science")
ax.hlines(totalEngTuit, 0, NUMBER_OF_MONTHS, color = "red", label = "Engineering")
ax.set(xticks = range(0, NUMBER_OF_MONTHS + 1, 12), xticklabels = xTickLabels)
ax.axis([0, NUMBER_OF_MONTHS + 1, 0, 100000])
ax.legend()
plt.title("Savings vs Tuition")
plt.ylabel("Amount $")
plt.xlabel("Years")
plt.show()
