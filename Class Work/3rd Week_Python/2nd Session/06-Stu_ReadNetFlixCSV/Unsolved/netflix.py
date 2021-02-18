# Modules
import os
import csv

# Prompt user for movie lookup
movie = input("What show or movie are you looking for? ")

# Set path for file
csvpath = os.path.join("..", "Resources", "netflix_ratings.csv")
found  = False
with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter = ',')
    
    for row in csv_reader:
        if row[0] == movie:
            print(row[0]+ " is rated " +row[1]+ " with rating of " +row[5])
            found =True
            break
    if found == False or found is False:
        print("Sorry, did not found the movie...")