# import directories
import csv  # provides functions for handling csv files
import os   # provides funtion for creating file path usable any operating system

# initialize variables 
totalVotes = 0

# create path to election_data.csv
filePath = os.path.join('Resources', 'election_data.csv')

# open election_data.csv file to read data
with open(filePath, 'r') as fileHeader:
    csvReader = csv.reader(fileHeader,delimiter = ',')

    # store CSV header
    csvHeader = next(csvReader)

    # set first data row as current row
    currentRow = next(csvReader)

    # increment totalVotes by 1
    totalVotes += 1

    # create a dictionary with candidate from the first row
    # key = candidate name
    # value = list of voter ids
    voting ={currentRow[2] : [currentRow[0]]}
    print(voting)

    # loop through data file
    for row in csvReader:
        # increment totalVotes by 1
        totalVotes += 1
        # if candidate in current row is in dictionary, append voter id to list
        if row[2] in voting:
            voting[row[2]].append(row[0])
        # if candidate in current row is not in dictionary, add candidate
        else:
            voting[row[2]] = [row[0]]
        

# Begin Printing
print(f'\nElection Results')
print(f'------------------------------')
print(f'Total Votes: {totalVotes}')
print(f'------------------------------')
# loop through dictionary to product data
    # calculate length
    # calculate percentage
    # print
print(f'------------------------------')
# determine winner

# print winner

# write output to text file