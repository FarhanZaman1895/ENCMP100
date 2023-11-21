## PERIHELION  Mercury's perihelion precession and general relativity
#
# In this lab assignment, a student completes a Python program to test with
# data an accurate prediction of Einstein’s theory, namely the perihelion
# precession of Mercury. Mercury’s orbit around the Sun is not a stationary
# ellipse, as Newton’s theory predicts when there are no other bodies. With
# Einstein’s theory, the relative angle of Mercury’s perihelion (position
# nearest the Sun) varies by about 575.31 arcseconds per century.
#
# Copyright (c) 2022, University of Alberta
# Electrical and Computer Engineering
# All rights reserved.
#
# Student name: Farhan Zaman (100%)
# Student CCID: fzaman2
# Others:
# 
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
from scipy import stats
import matplotlib.pyplot as plt
import csv, os

def main():
    data = loaddata('horizons_results')
    data = locate(data) # Perihelia
    data = select(data, 50, ('Jan','Feb','Mar'))
    data = refine(data, "horizons_results")
    makeplot(data, 'horizons_results')
    savedata(data, "horizons_results")

def loaddata(filename):

    # Reads the file and creates the data array, filtering out all the
    # non data rows
    # Args: name of file: str
    # Returns: data: list of dictionaries
    # Side Effects: Prints progress every 10000 datums, opens the main data file

    file = open(filename + '.txt', 'r')
    lines = file.readlines()
    file.close()

    noSOE = True
    num = 0
    data = []
    for line in lines:
        if noSOE:
            if line.rstrip() == "$$SOE":
                noSOE = False
        elif line.rstrip() != "$$EOE":
            num = num+1
            if num % 10000 == 0:
                print(filename,":",num,"line(s)")
            datum = str2dict(line)
            data.append(datum)
        else:
            break # for
    if noSOE:
        print(filename,": no $$SOE line")
    else:
        print(filename,":",num,"line(s)")

    return data

def str2dict(line):

    # Creates a dictionary based on a given string
    # Args: line from data: string
    # Return: dictionary: {float, str, tuple}
    # Side Effects: N/A

    lineArray = line.split(",")

    numdate = float(lineArray[0])
    strdate = lineArray[1].split(" ")[2]
    coord = (float(lineArray[2]), float(lineArray[3]), float(lineArray[4]))

    return { 'numdate': numdate, 'strdate': strdate, 'coord': coord }

def locate(data1):

    # Filters out data and outputs only the perihelions
    # Args: data: list
    # Return: filtered data: list
    # Side Effects: N/A

    dist = []
    for datum in data1:
        coord = np.array(datum['coord'])
        dot = np.dot(coord,coord)
        dist.append(np.sqrt(dot))
    data2 = []
    for k in range(1,len(dist)-1):
        if dist[k] < dist[k-1] and dist[k] < dist[k+1]:
            data2.append(data1[k])
    return data2

def select(data, ystep, month):

    # Filters the data based on the year being a multiple of y step, and for certain months
    # Args: data: list, ystep: int, month: tuple of str
    # Return: filtered data: list
    # Side Effects: N/A

    newData = []
    for datum in data:
        datumArray = datum['strdate'].split("-")
        if int(datumArray[0]) % ystep == 0 and datumArray[1] in month:
            newData.append(datum)
    return newData

def refine(data, filename):

    # Locates files in working directory and looks for ones related to the valid dates,
    # then creates a new dataset based on the new file data
    # Args: data: list, name of file to filter: str
    # Return: fileData: list
    # Side Effects: Opens files in working directory

    dirContents = []
    validStrDates = [datum["strdate"] for datum in data]

    for file in os.listdir():
        if filename in file and ".txt" in file and len(file.split("_")) == 3:
            isolateDate = file.replace(".txt", "").split("_")[2]
            if isolateDate in validStrDates:
                dirContents.append(file.replace(".txt", ""))

    fileData = [locate(loaddata(i))[0] for i in dirContents]
    fileData = sorted(fileData, key = lambda d: d["numdate"])

    return fileData

def makeplot(data, filename):

    # Creates the main plot for this program and saves as file
    # Args: data: list, file to save: str
    # Return: N/A
    # Side Effects: Displays and saves graph

    (numdate,strdate,arcsec) = precess(data)
    plt.plot(numdate,arcsec,'bo')
    plt.xticks(numdate,strdate,rotation=45)
    add2plot(numdate,arcsec)
    plt.xlabel("Perihelion date")
    plt.ylabel("Precession (arcsec)")
    plt.savefig(filename+'.png',bbox_inches='tight')
    plt.show()

def precess(data):

    # Calculates the perihelions for data and outputs multiple arrays
    # Args: data: list
    # Return: tuple of data lists
    # Side Effects: N/A

    numdate = []
    strdate = []
    arcsec = []
    v = np.array(data[0]['coord']) # Reference (3D)
    for datum in data:
        u = np.array(datum['coord']) # Perihelion (3D)
        ratio = np.dot(u,v)/np.sqrt(np.dot(u,u)*np.dot(v,v))
        if np.abs(ratio) <= 1:
            angle = 3600*np.degrees(np.arccos(ratio))
            numdate.append(datum['numdate'])
            strdate.append(datum['strdate'])
            arcsec.append(angle)
    return (numdate,strdate,arcsec)

def add2plot(numdate, actual):

    # Plots the line of best fit
    # Args: date values: list, original values: list
    # Return: N/A
    # Side Effects: stores plot to memory

    r = stats.linregress(numdate,actual)
    bestfit = []
    for k in range(len(numdate)):
        bestfit.append(r[0]*numdate[k]+r[1])
    plt.plot(numdate,bestfit,'b-')
    plt.legend(["Actual data","Best fit line"], loc = "upper left")

    slope = r[0] * 365.25 * 100

    plt.title("Slope of best fit line: %.2f arcsec/cent" % slope)

def savedata(data, filename):

    # Saves the data into a csv file using the standard csv dictionary writer
    # Args: data: list, file to save to: str
    # Returns: N/A
    # Side Effects: Opens a csv file, saves new data to csv file

    filename = filename + ".csv"

    with open(filename, "w") as csvfile:
        fieldnames = ["NUMDATE", "STRDATE", "XCOORD", "YCOORD", "ZCOORD"]
        writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

        writer.writeheader()

        for datum in data:
            tempData = {"NUMDATE": "%.6f" % round(datum["numdate"], 6), 
                        "STRDATE": datum["strdate"], 
                        "XCOORD": "%.6f" % round(datum["coord"][0], 6), 
                        "YCOORD": "%.6f" % round(datum["coord"][1], 6), 
                        "ZCOORD": "%.6f" % round(datum["coord"][2], 6)}

            writer.writerow(tempData)

    csvfile.close()

main()
