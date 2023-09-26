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
# Others: N/A
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
#
import numpy as np
import matplotlib.pyplot as plt

## EXPERIMENT DATA

# Data from NIST
data = [656.460,486.271,434.1692,410.2892, 397.1197, 389.0166, 383.6485] # nm
nist = np.array(data)
n = len(nist)

## MODEL SETUP

# Physics Constants
MASS_ELECTRON = 9.1093837e-31
ELEMENTARY_CHARGE = 1.6021766e-19
PERMITTIVITY = 8.8541878e-12
PLANK_CONSTANT = 6.6260702e-34
SPEED_OF_LIGHT = 2.9979246e8

# Calculation of Rydberg Constant
RYDBERG = (MASS_ELECTRON * (ELEMENTARY_CHARGE ** 4)) / (8 * (PERMITTIVITY ** 2) * (PLANK_CONSTANT ** 3) * SPEED_OF_LIGHT)

# Given Rydberg Constant = 1.0973732e7 # 1/m
print("Rydberg constant:", RYDBERG, "1/m")

## SIMULATION DATA

# Get values for nf and ni
nf = input("Final state (nf): ")
nf = int(nf)
ni = np.arange(nf+1,nf+n+1)

# Calculate Wavelengths

tempDenomenator = (1 / (nf ** 2)) - (1 / (ni ** 2))
wavelengths = (1 / (RYDBERG * tempDenomenator)) * 1e9

# This is an alternative solution I created that uses a for loop on an empty array
# wavelengths = np.empty(7) # Creates an empty array of size 7
# for i in range(7):
#     tempDenomenator = (1 / (nf ** 2)) - (1 / (ni[i] ** 2))
#     wavelengths[i] = (1 / (RYDBERG * tempDenomenator)) * 1e9

# Plots the NIST data as blue x
plt.plot(ni,nist,'bx', label = "NIST")

# Theoretical Calculation Plots
plt.plot(ni, wavelengths, "r+", label = "Theoretical")

# Graph Labels
plt.title("Hydrogen Emission Spectrum")
plt.xlabel("Initial state (ni)")
plt.ylabel("Wavelength (nm)")
plt.legend()
plt.grid(True)
plt.show()