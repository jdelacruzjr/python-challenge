## Importing Modules important for the analysis

# Module for creating file paths across Operating Systems
import os

# Module for reading CSV files
import csv

# Set relative path to collect data from csv file in Resources folder
data_path=os.path.join('Resources', 'election_data.csv')

# List to hold Candidate Names
candidates = []

# List to hold Number of Votes candidates receive
num_votes = []

# List to hold Percentage of Total Votes candidates receive
percent_votes = []

# Counter for Total Number of Votes
total_votes = 0

# Read csv file
with open(data_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Read Header row
    csv_header = next(csvreader)

    for row in csvreader:
        # Add to Counter for Total Number of Votes
        total_votes += 1
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1
    # Add to Percent of Total Votes
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = (percentage)
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    # Determine Winning Candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]

# Output Election Results to Terminal
print("Election Results")
print("-------------------------")
print(f"Total Votes: {str(total_votes)}")
print("-------------------------")
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
print("-------------------------")
print(f"Winner: {winning_candidate}")
print("-------------------------")

# Export Election Results to Text File
output_file = os.path.join('Analysis', 'Election_Results.txt')

Election_Results = open(output_file, "w")

line1 = "Election Results"
line2 = "------------------------"
line3 = str(f"Total Votes: {str(total_votes)}")
line4 = str("------------------------")
Election_Results.write('{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4))
for i in range(len(candidates)):
    line = str(
        f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    Election_Results.write('{}\n'.format(line))
line5 = "------------------------"
line6 = str(f"Winner: {winning_candidate}")
line7 = "------------------------"
Election_Results.write('{}\n''{}\n''{}\n'.format(line5, line6, line7))

#-------------------
#End Analysis