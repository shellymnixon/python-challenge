import os
import csv
import sys
csvpath = os.path.join("C:/Users/arc user/Desktop/python-challenge/PyBank/Resources/budget_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    print(header)
    total_months = 0
    total_profit = 0
    previous = 0
    change_list = []
    greatest_increase = ["", 99999]
    greatest_decrease = ["", 0]

    for row in csvreader:
        total_months = total_months + 1
        total_profit = total_profit + int(row[1])
        change = int(row[1]) - previous
        change_list.append(change)
        previous = int(row[1])
        len_list = len(change_list)-1

        if change> greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = change
        if change< greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = change
    average_change = round(sum(change_list[1:])/len_list, 2)
    
    
    print("Financial Analysis")
    print("--------------------------")
    print("Total Months: ",total_months) 
    print("Total: $",total_profit)
    print("Average Change: $",average_change)
    print("Greatest Increase in Profits: ", greatest_increase[0], greatest_increase[1])
    print("Greatest Decrease in Profits: ", greatest_decrease[0], greatest_decrease[1])
    
text_file = open("PyBank.txt", "w")
with open("PyBank.txt", "w") as text_file:
    print("Financial Analysis", file=text_file)
    print("---------------------------", file=text_file)
    print(f"Total Months: {total_months}", file=text_file)
    print(f"Total : ${total_profit}", file=text_file)
    print(f"Average Change: ${average_change}", file=text_file)    
    print(f"Greatest Increase in Profits: {greatest_increase[0]} {greatest_increase[1]}", file=text_file)
    print(f"Greatest Decrease in Profits: {greatest_decrease[0]} {greatest_decrease[1]}", file=text_file)