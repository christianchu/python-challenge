import os
import csv

csv_path = os.path.join("Resources", "election_data.csv")

with open(csv_path, newline="") as csvfile:
    #reader
    election_csv = csv.reader(csvfile, delimiter=",")
    #skip header
    next(election_csv,None)
    
    #set variables
    total_votes = []
    candidates = []
    pct_won = []
    total_won = []
    winner = []
    #loop through each row of election_csv
    for row in election_csv:
       #add 1 row for total number of votes
       total_votes.append(row[0])
       if row[2] not in candidates:
           #add candidate to list
           candidates.append(row[2])
           #index position of candidate
           candidates_index = candidates.index(row[2])
           #add 1 to thier vote
           total_won.append(row[0])
           
       else:
           #index position of candidate
           candidates_index = candidates.index(row[2])
           #add one and set that candidates index position
           total_won[candidates_index] =+ 1
           
    #print total number of rows(votes)       
    total_votes = len(total_votes)
    #max value winner
    winner = max(total_won)
    #set index of winner
    win_in = total_won.index(winner)
    #retrieve candidate name
    elected = candidates[win_in]

print(f"Election Results")
print(f"-------------------------")
print(f"Total Votes: {total_votes}")
print(f"-------------------------")
print(f"{candidates}: {total_won[candidates_index]}")
print(f"-------------------------")
print(f"Winner: {elected}")

f = open("analysis/Results.txt", "w")
f.write(f"Election Results\n")
f.write(f"-------------------------\n")
f.write(f"Total Votes: \n")
f.write(f"-------------------------\n")
f.write(f"names\n")
f.write(f"-------------------------\n")
f.write(f"Winner: \n")
f.close()