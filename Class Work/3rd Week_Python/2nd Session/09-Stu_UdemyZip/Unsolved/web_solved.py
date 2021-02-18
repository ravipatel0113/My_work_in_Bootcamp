import os
import csv

udemy_csv = os.path.join("..", "Resources", "web_starter.csv")

# Lists to store data
title = []
price = []
subscribers = []
reviews = []
review_percent = []
length = []

# Use encoding for Windows
with open(udemy_csv,  newline='', encoding='utf-8') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=',')
    for row in csv_reader:
        title.append(row[1])

        price.append(row[4])

        subscribers.append(row[5])

        reviews.append(row[6])

        percent =round(int(row[6])/ int(row[5]),2)
        review_percent.append(percent)
        new_length= row[9].split(" ")
        length.append(float(new_length[0]))

cleaned_csv = zip(title,price,subscribers,reviews,review_percent,length)
output_file = os.path.join("web_final_2.csv")

with open(output_file, 'w', newline="") as datafile:
    writer =csv.writer(datafile)

    writer.writerow(["Title","Price","subscribers","reviews","review_percent","length"])
    writer.writerows(cleaned_csv)
