import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join('..', 'Resources', 'WWE-Data-2016.csv')

# Define the function and have it accept the 'wrestlerData' as its sole parameter
def print_percentages(wrestlerData):
    name = str(wrestlerData[0])
    wins = int(wrestlerData[1])
    looses = int(wrestlerData[2])
    draw = int(wrestlerData[3])

# Find the total number of matches wrestled
    total = wins + looses+draw

# Find the percentage of matches won
    percentage_win = (wins/total) *100
# Find the percentage of matches lost
    percentage_lost = (looses/total) *100
# Find the percentage of matches drawn
    percentage_draw = (draw/total) *100
# Print out the wrestler's name and their percentage stats
   

    print(f'THE NAME OF WRESTLER IS: {name}')
    print(f'total matches played: {total}')
    print(f'Win percentage: {percentage_win}')
    print(f'Lost percentage: {percentage_lost}')
    print(f'Draw percentag: {percentage_draw}')
    if percentage_lost >= 50:
        print(f'{name} is a Jobber')
    else:
        print(f'{name} is a Superstar')
# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
