import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")

print(csvpath)

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    print(csvreader)
    csv_header = next(csvreader) 
    print(f"csv_header: {csv_header}")
  
    for row in csvreader:
        print(row)
