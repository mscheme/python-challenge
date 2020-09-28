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
        
# create path for output
output = os.path.join('analysis', 'election_results.txt')

# open election_data.csv file to read data
with open(output, 'w') as outputHeader:
    # write output to text file & print
    outputHeader.write('Election Results\n')
    print(f'\nElection Results')

    outputHeader.write('------------------------------\n')
    print(f'------------------------------')

    outputHeader.write('Total Votes: ' + str(totalVotes) +'\n')
    print(f'Total Votes: {totalVotes}')

    outputHeader.write('------------------------------\n')
    print(f'------------------------------')

    # loop through dictionary to produce and print data
    numKey = 0

    for candidate in voting.keys():
        # calculate length to determine number of votes for a candidate
        numVotes = len(voting[candidate])
        
        # calculate percentage
        perctVotes = format(round(numVotes/totalVotes * 100, 3), '.3f')

        # print
        outputHeader.write(candidate + ': ' + str(perctVotes) + '% (' + str(numVotes) + ')\n')
        print(f'{candidate}: {perctVotes}% ({numVotes})')

        numKey += 1
        
        # determine winner
        if numKey == 1:
            winner = candidate
            maxVotes = numVotes
        else:
            if numVotes > maxVotes:
                winner = candidate
                maxVotes = numVotes
    # print winner
    outputHeader.write('------------------------------\n')
    print(f'------------------------------')

    outputHeader.write('Winner: ' + winner + '\n')
    print(f'Winner: {winner}')

    outputHeader.write('------------------------------\n')
    print(f'------------------------------')
