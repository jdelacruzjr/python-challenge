## Importing Modules important for the analysis

# Module for creating file paths across Operating Systems
import os

# Module for reading CSV files
import csv

# Set relative path to collect data from csv file in Resources folder
data_path=os.path.join('Resources', 'budget_data.csv')

# Counter for Total Months in dataset
total_months = 0

# Counter for Total Profit & Loss
total_profit_loss = 0

# Counter to track value of Total Profit & Loss
value = 0

# Counter to track changes in Total Profit & Loss
change = 0



#----------------------------------------

## EXAMPLE SYNTAX ONLY!!!! Write a function that returns the arithmetic average for a list of numbers
def average(numbers):
    length = len(numbers)
    total = 0.0
    for number in numbers:
        total += number
    return total / length
    
    
## EXAMPLE SYNTAX ONLY!!!! Create a .txt file and write to that .txt file

# save the output file path (CREATE .TXT FILE)
output_file = os.path.join("Analysis_Results.txt")

# open the output file, create a header row, and then write the zipped object to the csv
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile)

    writer.writerow(["Index", "Employee", "Department"])

    writer.writerow(["1", "Michael", "Boss"])
    
    writer.writerow(["2", "Dwight", "Sales"])

    writer.writerow(["3", "Meredith", "Sales"])

    writer.writerow(["4", "Kelly", "HR"])
