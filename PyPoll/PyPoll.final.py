import os
import csv

poll_csv = os.path.join('Resources','election_data.csv')

with open(poll_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    poll_list = list(csvreader)

# split nested list into three lists
voterID_list, county_list, candidate_list = map(list, zip(*poll_list))

total_votes = len(voterID_list)
print("Election Results")
print("----------------------------")
print("Total Votes: "+ str(total_votes))
print("----------------------------")

# determine list of candidates who received votes
seen = set()
uniq = []
for x in candidate_list:
    if x not in seen:
        uniq.append(x)
        seen.add(x)

# total number of votes each candidate received
candidate_count = [[candidate,candidate_list.count(candidate)] for candidate in set(candidate_list)]

# percentage of total votes for each candidate
cand_sorted = sorted(candidate_count, key = lambda x: x[1], reverse=True)
percentage = float(0)
for (name,votes) in cand_sorted:
    percentage = (votes / total_votes)*100
    formatted_perc = '{:.3f}%'.format(percentage)
    print(str(name) + ": " + str(formatted_perc) + " (" + str(votes) + ")")

# winner of election based on popular vote
name_list, vote_list = map(list, zip(*cand_sorted))
winner = name_list[0]
print("----------------------------")
print("Winner: " + str(winner))
print("----------------------------")