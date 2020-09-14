import os
import csv
csvpath = os.path.join("C:/Users/arc user/Desktop/python-challenge/PyBank/Resources/budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(header)
    total_months = 0
    total_profit = 0
    for row in csvreader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
    average_change = round(total_profit/total_months, 2)
    
    print("Total Months: ",total_months) 
    print("Total: $",total_profit)
    print("Average Change: $",average_change)
    print("Greatest Increase in Profits:")
    print("Greatest Decrease in Profits:")
    import sys
    text_file = open("PyBank.txt", "w")
    with open("PyBank.txt", "w") as text_file:
        print(f"Total Months: {total_months}", file=text_file)
        print(f"Total : ${total_profit}", file=text_file)
        print(f"Average Change: ${average_change}", file=text_file)    
        print("Greatest Increase in Profits: ", file=text_file)
        print("Greatest Decrease in Profits: ", file=text_file)