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

# dictionary from : https://gist.github.com/afhaque/29f0f4f37463c447770517a6c17d08f5
statesABBV = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# with open(udemy_csv, encoding='utf-8') as csvfile:
with open(emp_csv) as fileHeader:
    csvReader = csv.reader(fileHeader, delimiter=",")

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

        # use dictionary to convert state to abbrv
        state.append(statesABBV[row[4]])

# combine strings
cleaned_empData = zip(empID, firstName, lastName, dob, ssn, state)

# set output file path
output = os.path.join("cleanedEmpData.csv")

# open output file
with open(output, "w") as outputHeader:
    writer = csv.writer(outputHeader)

    # write the header row
    writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

    # write zipped rows
    writer.writerows(cleaned_empData)