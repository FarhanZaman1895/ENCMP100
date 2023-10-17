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

## PREPROCESSING

# Imports
import matplotlib.pyplot as plt
import numpy as np

# Constants
NUMBER_OF_MONTHS = 12 * 18
START_AMOUNT = 2000
MONTHLY_CONTRIBUTION = 200
MONTHLY_INTEREST = 0.0625
TUITION_INTEREST = 0.07

# Variables
artTuition = [5550]
sciTuition = [6150]
engTuition = [6550]

# Initialize y axis for graph
monthlyAmount = [START_AMOUNT]

## SAVING cALCULATION

# This section cycles through all the months in 18 years and calculates the amount in the account
# accounting for both monthly interest and a static monthly contribution

for i in range(1, NUMBER_OF_MONTHS):
    # Calculates the amount for each month using the given formula
    monthlyAmount += [monthlyAmount[i - 1] + (monthlyAmount[i - 1] * (MONTHLY_INTEREST / 12)) + MONTHLY_CONTRIBUTION]

## TUITION CALCULATION

# This section calculates the monthly tution accounting for interst using a for loop to cycle through
# tution amount for each year for 22 years

for i in range(1, 22):
    artTuition += [ artTuition[i-1] * (1 + TUITION_INTEREST) ]
    sciTuition += [ sciTuition[i-1] * (1 + TUITION_INTEREST) ]
    engTuition += [ engTuition[i-1] * (1 + TUITION_INTEREST) ]

# These variables are initialized to calculate the sum of the last 4 years using the array created above
totalArtTuition = 0
totalSciTuition = 0
totalEngTuition = 0

# This for loop goes through the last 4 elements of the array and sums them together to get the final tution
# cost for four years after turning 18
for i in range(0, 4):
    totalArtTuition += artTuition[-(i + 1)]
    totalSciTuition += sciTuition[-(i + 1)]
    totalEngTuition += engTuition[-(i + 1)]

# Print outputs for version 1
print("Version 1 - Solution")
print(f"The savings amount is ${format(monthlyAmount[-1], '.2f')}")
print(f"The cost of the arts program is ${format(totalArtTuition, '.2f')}")
print(f"The cost of the science program is ${format(totalSciTuition, '.2f')}")
print(f"The cost of the engineering program is ${format(totalEngTuition, '.2f')}")
print("")

## OPTIMIZATION

# This secion first prompts the user for which program they would like savings optimization for and then
# simulates the final savings amount value for 216 months, going up in increments of 1, until the savings
# amount is sufficient to pay for the tuition for the selected program

print("Version 2 - Solution")

# Prompt user for program
desiredProgram = input("Enter a program 1.Arts, 2.Science, 3. Engineering :")

# This while loop ensures that the input is valid using a try except statement
# If the input is not valid, as in not an int and not between 1 and 3, the program will prompt for the 
# user to input a valid number
condition = True
while condition:
    try: # Tries to convert the input to int
        desiredProgram = int(desiredProgram)
    except: # If it fails, prompt again for an input
        print("Please enter an integer value")
        desiredProgram = input("Enter a program 1.Arts, 2.Science, 3. Engineering :")
    else:
        if desiredProgram in range(1, 4):
            # If the number is in the valid range, it breaks the loop
            condition = False
        else:
            # Prompts the user for a valid option
            print("Please enter a valid option.")
            desiredProgram = input("Enter a program 1.Arts, 2.Science, 3. Engineering :")

# Setup for the following while loop
condition = True
optimizeMonthlyContribution = 0

# Assigns the required amount to the selected program tuition, as well as the program name for the final
# print outputs
if desiredProgram == 1:
    requiredAmount = totalArtTuition
    programName = "arts"
elif desiredProgram == 2:
    requiredAmount = totalSciTuition
    programName = "science"
else:
    requiredAmount = totalEngTuition
    programName = "engineering"

# This while loop calculates the savings amount for 1 monthly contribution, and then adds 1 to 
# the monthly contribution until the final savings amount exceeds the required amount for the 
# program tuition.
while condition:
    optimizeMonthlyContribution += 1 # Adds 1 to the monthly contribution
    optimizeArray = [2000] # Resets the array for calculating monthly savings amount

    # Simulates the savings amount for the given monthly contribution amount
    for i in range(1, NUMBER_OF_MONTHS):
        optimizeArray += [optimizeArray[i - 1] + (optimizeArray[i - 1] * (MONTHLY_INTEREST / 12)) + optimizeMonthlyContribution]
    if optimizeArray[-1] >= requiredAmount:
        condition = False

# Tests if the monthly contribution required for the desired program is less than or equal to the 
# monthly contribution actually given of 200
if optimizeMonthlyContribution <= MONTHLY_CONTRIBUTION:
    print(f"Congratulation!!! You have saved enough for the {programName} program")
else:
    print(f"Unfortunately!!! You do not have enough saved for the {programName} program")

# Prints the optimal monthly contribution for the desired program
print(f"The optimal monthly contribution amount is ${optimizeMonthlyContribution}")

## PLOT

# This section creates a graph with 4 plots, one for the monthly savings amount with a contribution of $200 a month,
# and three horizontal lines for the prices of the four years of university after 18 years

# Make the labels for the ticks along x axis
# The np.char.mod function takes an array of any type and converts it into an array of strings
# I used this to create the labels for the x axis
xTickLabels = np.char.mod("%d", np.arange(0, 19))

# Plot Graph
fig, ax = plt.subplots() # This is a matplotlib object that is used to make the graph

# Plots the 4 graphs
ax.plot(range(0, NUMBER_OF_MONTHS), monthlyAmount, label = "Saving Balance")
ax.hlines(totalArtTuition, 0, NUMBER_OF_MONTHS, color = "orange", label = "Arts")
ax.hlines(totalSciTuition, 0, NUMBER_OF_MONTHS, color = "green", label = "Science")
ax.hlines(totalEngTuition, 0, NUMBER_OF_MONTHS, color = "red", label = "Engineering")

# This sets the x axis to show the years instead of months
ax.set(xticks = range(0, NUMBER_OF_MONTHS + 1, 12), xticklabels = xTickLabels)

# This removes the margins around the graph
ax.axis([0, NUMBER_OF_MONTHS + 1, 0, 100000])

# The legend placed in the lower right
ax.legend(loc = "lower right")

# Title and Axes
plt.title("Savings vs Tuition")
plt.ylabel("Amount $")
plt.xlabel("Years")

# Show the plot
plt.show()
