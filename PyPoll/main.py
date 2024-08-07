# Create Path 
import os 
import csv

csvpath = os.path.join("Resources", "election_data.csv")

# Define Variables
total_votes = 0
candidate_name = []
candidate_vote = {}
names = []

# Read CSV File
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader) 

# Calculate total votes and assign candidate name row
    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]

# Create list of names 
        if candidate_name not in names:
            names.append(candidate_name)
        if candidate_name in candidate_vote:
            candidate_vote[candidate_name] += 1
        else:
            candidate_vote[candidate_name] =1


# Calculate percentage of votes
results = []
for candidate, votes in candidate_vote.items():
    percentage = (votes / total_votes) * 100
    results.append(f'{candidate}: {percentage:.3f}% ({votes})')

# Calculate winner 
winner = max(candidate_vote, key=candidate_vote.get)

# Print Results
print("Election Results")
print("-------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------")
for result in results:
    print(result)
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")
