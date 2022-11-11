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

# Counter to track Value of Total Profit & Loss
value = 0

# Counter to track Changes in Total Profit & Loss
change = 0

# List to store Dates of financial activity in dataset
dates = []

# List to store Profits/Losses
profits = []

# Read csv file and Identify delimiter
with open(data_path, newline="") as budget_file:
    csvreader = csv.reader(budget_file, delimiter=",")
    
    # Read Header row
    csv_header = next(csvreader)
    
    # Go to First row
    first_row = next(csvreader)
    
    # Add Total Months counter
    total_months += 1
    
    # Add Total Profit & Loss counter
    total_profit_loss += int(first_row[1])
    value = int(first_row[1])
    
    # Read Rows after Header row
    for row in csvreader:
    
        # Get the Date
        dates.append(row[0])
        
        # Track Changes of Rows
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # Total Month Count
        total_months += 1
        
        # Calculate Net Total Profit & Loss Amount over entire period
        total_profit_loss = total_profit_loss + int(row[1])
        
        # Calculate Average Change in Amount for Profit & Loss over entire period
        avg_change = sum(profits)/len(profits)
        
    # Find Greatest Amount of Increase in Profit
    greatest_increase = max(profits)
    greatest_inc_index = profits.index(greatest_increase)
    greatest_inc_date = dates[greatest_inc_index]
        
    # Find Greatest Amount of Decrease in Profit
    greatest_decrease = min(profits)
    greatest_dec_index = profits.index(greatest_decrease)
    greatest_dec_date = dates[greatest_dec_index]
        
# Output Financial Analysis to Terminal
printoutput = (
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {str(total_months)}\n"
    f"Total: ${str(total_profit_loss)}\n"
    f"Average Change: ${str(round(avg_change,2))}\n"
    f"Greatest Increase in Profits: {greatest_inc_date} (${str(greatest_increase)})\n"
    f"Greatest Decrease in Profits: {greatest_dec_date} (${str(greatest_decrease)})\n")
print(printoutput)
        
# Export Financial Analysis to Text File
output_file = os.path.join('Analysis', 'Analysis_Results.txt')
        
Analysis_Results = open(output_file, "w")
        
line1 = "-----------------------"
line2 = "Financial Analysis"
line3 = "-----------------------"
line4 = str(f"Total Months: {str(total_months)}")
line5 = str(f"Total: ${str(total_profit_loss)}")
line6 = str(f"Average Change: ${str(round(avg_change,2))}")
line7 = str(f"Greatest Increase in Profits: {greatest_inc_date} (${str(greatest_increase)})")
line8 = str(f"Greatest Decrease in Profits: {greatest_dec_date} (${str(greatest_decrease)})")
Analysis_Results.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1, line2, line3, line4, line5, line6, line7, line8))

#-------------------
#End Analysis
