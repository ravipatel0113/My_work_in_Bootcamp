# Dependencies
import os
import csv

# Specify the file to write to
output_path = os.path.join("..", "output", "new2.csv")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['First Name', 'Last Name', 'SSN'])
    csvwriter.writerow("Hello World")
    # Write the second row
    csvwriter.writerow(['Caleb', 'Frost', '505-80-2901'])
    csvwriter.writerows(['Ravi', 'Patel', '520-452-4785']) # print each word differently kind of joke...
