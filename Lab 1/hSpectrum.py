## HSPECTRUM  Quantum Chemistry and the Hydrogen Emission Spectrum
#
# The periodic table is central to chemistry. According to Britannica,
# "Detailed understanding of the periodic system has developed along with
# the quantum theory of spectra and the electronic structure of atoms,
# beginning with the work of Bohr in 1913." In this lab assignment, a
# University of Alberta student explores the Bohr model's accuracy in
# predicting the hydrogen emission spectrum, using observed wavelengths
# from a US National Institute of Standards and Technology database.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Farhan Zaman
# Student CCID: fzaman2
# Others: 
# Vincent Chan (1%)
# Farhan Zaman (99%)
#
# To avoid plagiarism, list the names of persons, Version 0 author(s)
# excluded, whose code, words, ideas, or data you used. To avoid
# cheating, list the names of persons, excluding the ENCMP 100 lab
# instructor and TAs, who gave you compositional assistance.
#
# After each name, including your own name, enter in parentheses an
# estimate of the person's contributions in percent. Without these
# numbers, adding to 100%, follow-up questions will be asked.
#
# For anonymous sources, enter pseudonyms in uppercase, e.g., SAURON,
# followed by percentages as above. Email a link to or a copy of the
# source to the lab instructor before the assignment is due.

# Imports
import numpy as np
import matplotlib.pyplot as plt

## EXPERIMENT DATA

# Data from NIST
data = [656.460,486.271,434.1692,410.2892, 397.1197, 389.0166, 383.6485] # nm
nistWavelengths = np.array(data)
n = len(nistWavelengths)

## MODEL SETUP

# Physics Constants
MASS_ELECTRON = 9.1093837e-31
ELEMENTARY_CHARGE = 1.6021766e-19
PERMITTIVITY = 8.8541878e-12
PLANK_CONSTANT = 6.6260702e-34
SPEED_OF_LIGHT = 2.9979246e8
MASS_PROTON = 1.6726219e-27

# Calculation of Rydberg Constant
OLD_RYDBERG = (MASS_ELECTRON * (ELEMENTARY_CHARGE ** 4)) / (8 * (PERMITTIVITY ** 2) * (PLANK_CONSTANT ** 3) * SPEED_OF_LIGHT)

# Modify the Rydberg constant to account for proton mass
RYDBERG = OLD_RYDBERG * (MASS_PROTON / (MASS_PROTON + MASS_ELECTRON))

# Given Rydberg Constant = 1.0973732e7 # 1/m
print("Rydberg constant:", np.round(RYDBERG), "m"+chr(8315)+chr(185))

## SIMULATION DATA

# Get values for nf and ni
nf = input("Final state (nf): ")
nf = int(nf)
ni = np.arange(nf+1,nf+n+1)

# Calculate Wavelengths

tempDenomenator = (1 / (nf ** 2)) - (1 / (ni ** 2))
bohrWavelenghts = (1 / (RYDBERG * tempDenomenator)) * 1e9

# This is the code for the graph from version 1

# Plots the NIST data as blue x
# plt.plot(ni,nistWavelengths,'bx', label = "NIST")

# Theoretical Calculation Plots
# plt.plot(ni, bohrWavelenghts, "r+", label = "Theoretical")

# Graph Labels
# plt.title("Hydrogen Emission Spectrum")
# plt.xlabel("Initial state (ni)")
# plt.ylabel("Wavelength (nm)")
# plt.legend()
# plt.grid(True)
# plt.show()

## ERROR ANALYSIS

# Create an array of the error difference, NIST - Bohr
errorDifference = nistWavelengths - bohrWavelenghts

# Print the worse case error
maxError = np.max(np.abs(errorDifference))
print("Worse-case error: " + format(np.round(maxError, 3), ".3f") + " nm")

# Plot bar graph
plt.bar(ni, errorDifference, label = "NIST - Bohr")

# Graph Labels
plt.title("Error Difference between NIST and Bohr")
plt.xlabel("Initial state (ni)")
plt.ylabel("Wavelength difference (nm)")
plt.legend()
plt.show()
