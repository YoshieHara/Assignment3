# The total number of votes cast
# A complete list of candidates who received votes
# The percentage of votes each candidate won
# The total number of votes each candidate won
# The winner of the election based on popular vote

#import modules for using functions
import os
import csv

#Set the path of reading and saving files
csvpath = os.path.join("Resources", "election_data.csv")
outpath = os.path.join( "Analysis", "election_results.txt")

#Set variables
total_votes = 0
candidate_votes = {}


# Read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile)
    # Skip the header row
    next(csvreader)  

    # Count the votes for each candidate
    for row in csvreader:
        candidate_name = row[2]

        # Add the vote count if the candidate's name is already in the list
        if candidate_name in candidate_votes:
            candidate_votes[candidate_name] += 1
        # If this is the first vote the candidate got, start the count from 1
        else:
            candidate_votes[candidate_name] = 1

        # Add the total vote count
        total_votes += 1

# Determine the winner
winner = max(candidate_votes, key=candidate_votes.get)

# Print the results
print("Election Results")
print("-------------------------")
print("Total Votes:", total_votes)
print("-------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(candidate, ":", f"{percentage:.3f}%", votes)
print("-------------------------")
print("Winner: ", winner)
print("-------------------------")

#  Export a text file with the results to Analysis folder.
with open(outpath, "w") as outfile:
    outfile.write("Election Results\n")
    outfile.write("----------------------------\n")
    # Write the results to the text file
    outfile.write("Total Votes: " + str(total_votes) + "\n")
    outfile.write("----------------------------\n")
    outfile.write("Candidate Votes and Percentages:\n")
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        outfile.write(candidate + ": " + "{:.3f}".format(percentage) + "% (" + str(votes) + " votes)\n")
    outfile.write("----------------------------\n")
    outfile.write("Winner: " + winner + "\n")
    outfile.write("----------------------------\n")