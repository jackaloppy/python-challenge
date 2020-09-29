# Import Modules
import os
import csv

# Set the path
filepath = os.path.join("Resources","budget_data.csv")

# Open the CSV file
with open(filepath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skp the header row
    next(csvreader)
    
    month = 0
    total = 0
    maxpro = 0
    minpro = 0

    for row in csvreader:
        month += 1
        total += int(row[1])
        if maxpro < int(row[1]):
            maxpro = int(row[1])
            maxmon = row[0]
        if minpro > int(row[1]):
            minpro = int(row[1])
            minmon = row[0]   

f = open("analysis/output.txt", "a")
print("Financial Analysis", file =f)
print("----------------------------", file = f)
print("Total Months: " + str(month), file = f)
print("Total: $" + str(total), file=f)
print("Average Change: $" + str(total/month), file = f)
print("Greatest Increase in Profits: " + maxmon + " ($" + str(maxpro) +")", file =f)
print("Greatest Decrease in Profits: " + minmon + " ($" + str(minpro) +")", file =f)
f.close()

print("Financial Analysis")
print("----------------------------")
print("Total Months: " + str(month))
print("Total: $" + str(total))
print("Average Change: $" + str(total/month))
print("Greatest Increase in Profits: " + maxmon + " ($" + str(maxpro) +")")
print("Greatest Decrease in Profits: " + minmon + " ($" + str(minpro) +")")