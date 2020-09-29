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
        # Count the vote by each row
        vote_count += 1
        # Add candidate into dict key if it's not in there, starting with 0 vote.
        if row[2] not in candidate:
            candidate[row[2]] = 0
        # Add value(vote count) by 1 for matched key(candidate) in this dict. 
        candidate[row[2]] = candidate[row[2]] + 1
    # Find out the winner by using max function. 
    # Max first part is the items to compare i.e the key in dict
    # Max second part is the single argument function given to the item. So we apply dict.get function to 
    # the first part, which gives us the key (the vote counts) to compare. 
    winner = max(candidate, key=candidate.get)
    
    print("Election Results \n-------------------------")
    print("Total Votes: " + str(vote_count) + "\n-------------------------")
    for key in candidate:
        print(key + ": " + str("{:.3%}".format(candidate[key]/vote_count)) + " (" + str(candidate[key]) + ")")
    print("-------------------------" + "\nWinner: " + winner + "\n-------------------------")

f = open("analysis/output.txt", "a")
print("Election Results \n-------------------------", file = f)
print("Total Votes: " + str(vote_count) + "\n-------------------------", file = f)
for key in candidate:
    print(key + ": " + str("{:.3%}".format(candidate[key]/vote_count)) + " (" + str(candidate[key]) + ")" , file = f)
print("-------------------------" + "\nWinner: " + winner + "\n-------------------------", file = f)