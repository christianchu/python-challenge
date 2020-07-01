import os
import csv

csv_path = os.path.join("Resources", "budget_data.csv")

#open csv
with open(csv_path, newline="") as csvfile:
    budget_csv = csv.reader(csvfile, delimiter=",")
    #skip header
    next(budget_csv, None)
    
    total_months = []
    total_amount = []
    months = []
    average_change = []
    largest_increase = []
    largest_decrease = []
    
    for row in budget_csv:
        total_months.append(row[0])
        months.append(row[0])
        total_amount.append(int(row[1]))
        
    for i in range(len(total_amount)-1):
        average_change.append(total_amount[i+1]-total_amount[i])   
        #greatest / lowest change in profits
        #largest_change.append(total_amount[i+1]-total_amount[i])
        
    largest_increase = max(average_change)
    largest_decrease = min(average_change)
    total_months = len(total_months)
       
print(f"Financial Analysis")
print(f"----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${sum(total_amount)}")
print(f"Average Change: ${round(sum(average_change) / len(average_change), 2)}")
print(f"Greatest Increase in Profits: {months[average_change.index(max(average_change))+1]} (${largest_increase})")
print(f"Greatest Decrease in Profits: {months[average_change.index(min(average_change))+1]} (${largest_decrease})")

f = open("analysis/Results.txt", "w")
f.write(f"Financial Analysis\n")
f.write(f"----------------------------\n")
f.write(f"Total Months: {total_months}\n")
f.write(f"Total: ${sum(total_amount)}\n")
f.write(f"Average Change: ${round(sum(average_change) / len(average_change), 2)}\n")
f.write(f"Greatest Increase in Profits: {months[average_change.index(max(average_change))+1]} (${largest_increase})\n")
f.write(f"Greatest Decrease in Profits: {months[average_change.index(min(average_change))+1]} (${largest_decrease})\n")
f.close()