# import directories
import csv  # provides functions for handling csv files
import os   # provides funtion for creating file path usable any operating system

# initialize variables 
totalMonths = 0
total = 0
change = []
greatestIncrease = ['date', 0]
greatestDecrease = ['date', 0]

# create path to budget_data.csv
filePath = os.path.join('Resources', 'budget_data.csv')

# open budget_data.csv file to read data
with open(filePath, 'r') as fileHeader:
    csvReader = csv.reader(fileHeader,delimiter = ',')

    # store CSV header
    csvHeader = next(csvReader)

    # set first data row as current row
    currentRow = next(csvReader)

    # increment total months by 1
    totalMonths +=1 

    #add the row profit/loss to total
    total += int(currentRow[1])

    for row in csvReader:
        # set currentRow list to previousRow
        previousRow = currentRow

        # store next row of csv data as currentRow
        currentRow = row

        # calculate monthly change
        monthlyChange = int(currentRow[1]) - int(previousRow[1])

        # add monthly change to list
        change.append(monthlyChange)

        # add to the total
        total += int(currentRow[1])

        # increment the total number of months
        totalMonths += 1

        #if change is positive, compare to greatest increase in profits
        if monthlyChange > 0:
            # if current monthly change is greater than stored value, update
            if monthlyChange > greatestIncrease[1]:
                greatestIncrease[0] = currentRow[0]
                greatestIncrease[1] = monthlyChange
        #else if change is negative, compare to greatest decrease in losses
        elif monthlyChange < 0:
            #if current monthly change is less than stored value, update
            if monthlyChange < greatestDecrease[1]:
                greatestDecrease[0] = currentRow [0]
                greatestDecrease[1] = monthlyChange

# calculate sum of monthly changes
sumChange = sum(change)

# calculate length of months changes
length = len(change)

# calculate average of monthly changes
averageChange = sumChange/length

# display financial analysis
print(f'\nFinancial Analysis')
print(f'------------------------------')
print(f'Total Months: {totalMonths}')
print(f'Total: ${total}')
print(f'Average Change: ${round(averageChange,2)}')
print(f'Greatest Increase in Profits: {greatestIncrease[0]} (${greatestIncrease[1]})')
print(f'Greatest Decrease in Profits: {greatestDecrease[0]} (${greatestDecrease[1]})\n')

# Export Analysis as text file

# create file path for export
output_path = os.path.join('analysis', 'financialOutput.txt')

# write to text file

with open(output_path, 'w') as outputHeader:
    outputHeader.write('Financial Analysis\n')
    outputHeader.write('------------------------------\n')
    outputHeader.write('Total Months: ' + str(totalMonths)+'\n')
    outputHeader.write('Total: $' + str(total)+'\n')
    outputHeader.write('Average Change: $'+ str(round(averageChange,2))+'\n')
    outputHeader.write('Greatest Increase in Profits: '+ greatestIncrease[0]+ ' ($'+str(greatestIncrease[1])+')\n')
    outputHeader.write('Greatest Increase in Profits: '+ greatestDecrease[0]+ ' ($'+str(greatestDecrease[1])+')')



