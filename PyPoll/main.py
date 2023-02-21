import os
import csv

# Path to collect data from the Resources folder
budget_csv = os.path.join("/Users/srabanaguha/GitHub/python-challenge/PyPoll/Resources/election_data.csv")
output_path = os.path.join("/Users/srabanaguha/GitHub/python-challenge/PyPoll/output.txt")
total_votes = 0
candidates = {}
winner = ""

# Read in the CSV file
with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader) #skip header


    # Loop through each row in the csv file
    for row in csvreader:
        total_votes = total_votes + 1 #count total number of votes
        # Add the candidate to the dictionary of candidates
        candidate = row[2] 
        if candidate not in candidates:
            candidates[candidate] = 0

        # Count the number of votes each candidate received
        candidates[candidate] = candidates[candidate] + 1

  
            
# Print results to terminal
print("Election Results")
print("-----------------")
print(f"Total Votes : {total_votes}")
print("-----------------")
for candidate, votes in candidates.items():
    percentage = votes / total_votes * 100
    print(f"{candidate}: {percentage:.3f}% ({votes})")
     # Determine the winner based on popular vote
    if votes > candidates.get(winner, 0):
        winner = candidate
print("-------------------------")
print(f"Winner: {winner}")
print("-------------------------")



# Save the results to a text file
with open (output_path, 'w', newline='') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {total_votes}\n")
    text_file.write("-------------------------\n")
    for candidate, votes in candidates.items():
        percentage = votes / total_votes * 100
        text_file.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {winner}\n")
    text_file.write("-------------------------\n")

        
       

