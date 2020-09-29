# Import Modules
import os
import csv

# Set the path
filepath = os.path.join("Resources","election_data.csv")

# Open the CSV file
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip the header row
    next(csvreader)

    vote_count = 0
    candidate = {}
    
    for row in csvreader:
        vote_count += 1
        if row[2] not in candidate:
            candidate[row[2]] = 0
        candidate[row[2]] = candidate[row[2]] + 1

    print("Election Results \n-------------------------")
    print("Total Votes: " + str(vote_count) + "\n-------------------------")
    for key in candidate:
        print(key + ": " + str("{:.3%}".format(candidate[key]/vote_count)) + " (" + str(candidate[key]) + ")")
    print("-------------------------" + "\nWinner: " + max(candidate, key=candidate.get) + "\n-------------------------")

f = open("analysis/output.txt", "a")
print("Election Results \n-------------------------", file = f)
print("Total Votes: " + str(vote_count) + "\n-------------------------", file = f)
for key in candidate:
    print(key + ": " + str("{:.3%}".format(candidate[key]/vote_count)) + " (" + str(candidate[key]) + ")" , file = f)
print("-------------------------" + "\nWinner: " + max(candidate, key=candidate.get) + "\n-------------------------", file = f)