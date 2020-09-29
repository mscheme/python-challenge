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

        # store last name
        lastName.append(row[1][space+1:])

        # reformat DOB
        month = row[2][5:7]
        day = row[2][-2:]
        year = row[2][0:4]
        date = month + '/' + day + '/' + year

        # store DOB
        dob.append(date)

        # ssn reformat
        newSSN = '***-**-' + row[3][-4:]

        # store SSN
        ssn.append(newSSN)

        print(f'{empID[pos]}, {firstName[pos]}, {lastName[pos]}, {dob[pos]}, {ssn[pos]}')

        pos += 1

