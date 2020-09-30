# python-challenge
This repository contains three python assignments for a data analytics bootcamp.

In each of the three assignment folders (PyBank, PyBoss, and PyPoll) you will find a main.py file, a folder called 'Resources' which contains the data csv file for each assignment, and a folder called 'analysis' which contains the output of the programs.

The instructions provided for PyBank and PyPoll can be found in the Instructions.md file.
The instructions provided for PyBoss can be found in the PyBoss folder, file named PyBoss_Instructions.md.

PyBank - reads a csv file, stores the header, and reads each line of the csv file to determine: total number of months, the total profit/loss, average change between months, the month with the greatest profit increase, and the month with the greadest decrease in profits.
The change between each month was stored in a list. The length and sum of the list were then used to calculate the average change.
The results are printed in the terminal window. A text file of the results is also created and stored in the analysis folder.

PyPoll - reads a csv file, stores the header, and reads each line of the csv file to determine: total number of votes, votes per candidate, percentage of votes per candidate, and the winner of the election. The winner was determined by popular vote.
I did not assume to know the candidates prior to the program reading the data.
Using the first row of data I created a dictionary. I then looped through all of the lines in the csv file and compared the candidate to the existing keys of the dictionary.
If the key exists, the voter id is appended to the list of values for the key.
If the key does not exist, the candidate is added as a key to the dictionary and a list of voter id's is created.
Once the data is read, the length of the list for each key (candidate) is calculated and used to determine the candidate's vote count and percantage of the total votes. Using the individual candidate's vote count, a winner is determined.
The results are printed in the terminal window. A text file of the results is also created and stored in the analysis folder.

PyBoss - reads a csv file, stores the header, and reads each line of the csv file.
When each line of the csv file is read: the data is reformated or split and appended to individual lists.
Once all of the data is read and the lists are created, the lists are zipped together.
The cleaned data is then written into a csv file in the analysis folder.
