# This is main.py in PyPoll

import os 
import csv

candidates = []
num_votes = 0
vote_counts = []

filename = input("election_data.csv")

filepath = os.path.join("election_data.csv")
with open(filepath, 'r', newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)


    for row in csvreader:

        num_votes = num_votes + 1

        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1

        else:
            candidates.append(candidate)
            vote_counts.append(1)


percentages = []
max_votes = vote_counts[0]
max_index = 0

for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/num_votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

percentages = [round(i,2) for i in percentages]

print("Election Results")
print("----------------------")
print(f"Total Votes: {num_votes}")
print("----------------------")
for count in range(len(candidates)):
    print(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})")
print("----------------------")
print(f"Winner: {winner}")
print(f"---------------------")



save_file = filename.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath, 'w') as text:
    text.write("Election Results" + "\n")
    text.write("----------------------" + "\n")
    text.write(f"Total Votes: {num_votes}" + "\n")
    text.write("----------------------" + "\n")
    for count in range(len(candidates)):
        text.write(f"{candidates[count]}: {percentages[count]}% ({vote_counts[count]})" + "\n")
    text.write("----------------------" + "\n")
    text.write(f"Winner: {winner}" + "\n")
    text.write("----------------------" + "\n")



