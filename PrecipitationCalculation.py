# # CS 101
# # Prog5.py
# # Program 5
# # Lia Vang
# # lvp4b@mail.umkc.edu
# #
# # PROBLEM: Calculate the average monthly precipitation and total precipitation per month
# #
# # ALGORITHM:
# #      1. Ask the user for the precipitation file to read
# #           If the file is not found:
# #              Warn the user and ask them to choose a new file
# #      2. Open the precipitation file for reading
# #           If the file has an I/O error:
# #              Warn the user
# #                 Ask them to choose a new file
# #      3. Group the sum of the precipitation on each line in the precipitation
# #         file by the year and monthlyAverages and store it in a dictionary with a key in YYYYMM format
# #           Ignore precipitation values that aren't a float
# #      4. Close the precipitation file
# #      5.  Ask the user for the output filename
# #      6.  Open the output file for writing
# #            If the file can't be opened for writing:
# #          Warn the user and ask them to choose a new file
# #            If the file already exists, overwrite it without asking
# #      7. Sort the dictionary by key in ascending order
# #      8. For each entry in the sorted dictionary:
# #          Write a new line to the output file with the key and value separated by a comma
# #      9. Close the output file
# #      10. Group the sum and the count of the values of each entry in the dictionary by monthlyAverages and store it in a new dictionary with an integer key
# #      11. For each monthlyAverages number from 1 to 12:
# #            Calculate the average using the new dictionary and store it in an average dictionary
# #            If data for a monthlyAverages doesn't exist, store 0 in the average dictionary as for that monthlyAverages
# #      12. Display a header for the monthly month averages and the headers for two columns of information
# #      13. Sort the average dictionary by key in ascending order
# #      14. For each entry in the sorted average dictionary:
# #            Find the abbreviated name of the monthlyAverages corresponding to the key
# #              Print a line containing the abbreviated monthlyAverages name followed by average precipitation
# #      15. Extra Credit: Plot the total monthly averages on a graph
# # ERROR HANDLING:
# #     Input validation. Incorrect inputs within a file is ignored.

import os.path
import pylab

# Ask the user for the precipitation file
def getPrecipitationFile():
    while True:
        try:
            filename = input("Enter the file with precipitation data ==> ")

            if not os.path.exists(filename):
                print("The file specified could not be found")
                continue
            return open(filename)
        except IOError:
            print("The file specified has an IO Error")

# Group the sum of precipitations by month in a dictionary with a key in YYYYMM format
def getPrecipitationPerYearMonth(file):
    result = {}
    for line in file:
        try:
            if line.find(",") == -1:
                continue

            columns = line.split(",")
            date = columns[0][:6]
            precipitation = float(columns[1].rstrip())

            result[date] = result.get(date, 0) + precipitation;
        except ValueError:
            pass
    return result

# Opens the output file specified by the user
def getOutputFile():
    while True:
        try:
            filename = input("Enter the monthly data file to save to. ==> ")
            return open(filename, "w")
        except IOError:
            print("The file specified has an IO Error")

# Calculates the total monthly average precipitation
def getMonthlyAverages(precipitationPerMonth):
    averages = {}
    for date in precipitationPerMonth:
        month = int(date[4:])
        
        if month not in averages:
            averages[month] = [0, 0]
             
        averages[month][0] += precipitationPerMonth[date]
        averages[month][1] += 1

    for month in averages:
        averages[month] = averages[month][0] / averages[month][1]
    
    return averages

# Displays the monthly total averages
def displayMonthlyAverages(monthlyAverages):
    print("\n      Monthly Total Averages\n")
    print("{:>9}{:>20}".format("Month", "Avg Precip"))
    print("{:>9}{:>20}".format("=====", "=========="))
      
    for month in range(1, 13):
        print("{:>9}{:>20.4f}".format(getMonthName(month), monthlyAverages.get(month, 0)))

# Plots the monthly total averages (Extra Credit)
def plotMonthlyAverages(monthlyAverages):
    pylab.plot([monthlyAverages.get(m, 0) for m in range(1, 13)])
    pylab.xlabel("Month")
    pylab.ylabel("Precip (mm)")
    pylab.xticks(range(0, 12), [getMonthName(m) for m in range(1 , 13)])
    pylab.title("Montly Total Averages")
    pylab.show()

# Gets the name of a month from the specified month number (1..12)
def getMonthName(month):
    return {1 : "Jan", 2 : "Feb", 3 : "March", 4 : "April", 5 : "May",
             6 : "June", 7 : "July", 8 : "Aug", 9 : "Sept", 10 : "Oct",
             11 : "Nov", 12 : "Dec"}[month]

with getPrecipitationFile() as precipitationFile:
    precipitationPerYearMonth = getPrecipitationPerYearMonth(precipitationFile)

with getOutputFile() as outputFile:
    for date in sorted(precipitationPerYearMonth):
        outputFile.write(date + "," + str(precipitationPerYearMonth[date]) + "\n")

monthlyAverages = getMonthlyAverages(precipitationPerYearMonth)
displayMonthlyAverages(monthlyAverages)
plotMonthlyAverages(monthlyAverages)
