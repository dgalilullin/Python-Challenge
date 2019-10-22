import os
import csv
#csv_path = os.path.join("..","PyPoll","election_data.csv")
csv_path = r"C:\Users\dgali\Documents\GitHub\Python-Challenge\PyPoll\election_data.csv"
with open (csv_path, newline="") as csvfile:
    file_reader = csv.reader (csvfile,delimiter=",")   
    #lst = list (rows)
    #print (lst)
    total_votes = -1
    candidates_and_votes = {}    
    for every_row in file_reader:
        total_votes = total_votes + 1
        candidate = every_row[2]
        if candidate not in candidates_and_votes:
            candidates_and_votes [candidate]=0
        candidates_and_votes [candidate] +=1
print ("Election Results")
print ("---------------------")
print(f'Total votes: {total_votes}')
print ("---------------------")
candidates_and_votes.pop ("Candidate")
for candidate in candidates_and_votes:
    print(f"{candidate}: {round(candidates_and_votes[candidate]/total_votes*100,3)}% ({candidates_and_votes[candidate]})")
print ("---------------------")
vote=list(candidates_and_votes.values())
cand=list(candidates_and_votes.keys())
winner = cand[vote.index(max(vote))]
print (f"Winner:{winner}")
f = open(r"C:\Users\dgali\Documents\GitHub\Python-Challenge\PyPoll\summary.txt",'w')
f.write ("Election Results"+"\n")
f.write ("---------------------"+"\n")
f.write ("Total votes: "+str(total_votes)+"\n")
f.write ("---------------------"+"\n")
for candidate in candidates_and_votes:
    f.write(f"{candidate}: {round(candidates_and_votes[candidate]/total_votes*100,3)}% ({candidates_and_votes[candidate]})\n")
f.write ("---------------------"+"\n")
f.write (f"Winner: {winner}")
f.close()