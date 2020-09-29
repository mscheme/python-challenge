# import directories
import os
import csv

# path to data file
emp_csv = os.path.join("Resources", "employee_data.csv")

# Lists to store data
empID = []
firstName = []
lastName = []
dob = []
ssn = []
state = []
pos = 0

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(emp_csv) as fileHeader:
    csvReader = csv.reader(fileHeader, delimiter=",")
    # store CSV header
    csvHeader = next(csvReader)

    for row in csvReader:

        # read employee id
        empID.append(row[0])

        # read name find index for space
        space = row[1].find(' ')
        
        # store first name
        firstName.append(row[1][0:space])
        print(firstName[pos])

        # store last name
        lastName.append(row[1][space+1:])
        print(lastName[pos])

        pos += 1


