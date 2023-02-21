import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("/Users/srabanaguha/GitHub/python-challenge/PyBank/Resources/budget_data.csv")
output_path = os.path.join("/Users/srabanaguha/GitHub/python-challenge/PyBank/output.txt")
total_months = 0
total_pl = 0
average_change = []
total_avg_change = 0
prev_pl = 0
greatest_inc_profit = 0
greatest_dec_profit = 0

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #skip header


    # Loop through the data
    for row in csvreader:

        
        total_months = total_months + 1
        total_pl = round(total_pl + float(row[1]))
       
        if total_months != 1:
            average_change.append( float(row[1])- prev_pl )
       
        if(float(row[1]) - prev_pl > greatest_inc_profit):
            greatest_inc_profit = round(float(row[1]) - prev_pl)
            greatest_inc_month = row[0]
        if(float(row[1]) - prev_pl < greatest_dec_profit):
            greatest_dec_profit = round(float(row[1]) - prev_pl )
            greatest_dec_month = row[0]

        prev_pl = float(row[1])
       
total_avg_change = round(sum(average_change)/len(average_change) ,2)

print("Financial Analysis")
print("--------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_pl}")
print(f"Average Change : ${total_avg_change}")
print(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_profit})")
print(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec_profit})")

# Save the results to a text file
with open (output_path, 'w', newline='') as text_file:
    text_file.write("Financial Analysis\n")
    text_file.write("--------------------\n")
    text_file.write(f"Total Months : {total_months}\n")
    text_file.write(f"Total: ${total_pl}\n")
    text_file.write(f"Average Change : ${total_avg_change}\n")
    text_file.write(f"Greatest Increase in Profits: {greatest_inc_month} (${greatest_inc_profit})\n")
    text_file.write(f"Greatest Decrease in Profits: {greatest_dec_month} (${greatest_dec_profit})\n")