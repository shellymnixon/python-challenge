import os
import csv 
import sys
csvpath = os.path.join("C:/Users/arc user/Desktop/python-challenge/PyPoll/Resources/election_data.csv")
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    #print(header)
    total_votes = 0
    candidate_list = []
    candidate_dictionary = {}
    winning_count = 0
    winner = ""
    for row in csvreader:
        total_votes = total_votes + 1
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            candidate_dictionary[row[2]]=0
        candidate_dictionary[row[2]]=candidate_dictionary[row[2]] +1
    #print(candidate_dictionary)
    print("Election Results")
    print("---------------------------")
    print("Total Votes:", total_votes)
    print("---------------------------")
    text_file = open("PyPoll.txt", "w")
with open("PyPoll.txt", "w") as text_file:
    print("Election Results", file=text_file)
    print("---------------------------", file=text_file)
    print(f"Total Votes: {total_votes}", file=text_file)
    print("---------------------------", file=text_file)
    for x in candidate_dictionary:
        votes = candidate_dictionary.get(x)
        vote_percentage = round(float(votes) / float(total_votes) * 100, 3)
        
        print(x, vote_percentage,"%", votes)
        print(f"{x} {vote_percentage}% {votes}", file=text_file)
        if (votes > winning_count):
            winning_count = votes
            winner = x
    
    print("---------------------------")
    print("Winner:", winner)
    print("---------------------------")
    
    print("---------------------------", file=text_file)
    print(f"Winner: {winner}", file=text_file)
    print("---------------------------", file=text_file)