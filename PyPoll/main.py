#Import all library needed
import os
import csv

#initiate all values needed
totalVotes=0
candidates=[]
candidatesVote=[]
candidatePer=[]

#Find and open the csv file
cwd = os.getcwd()
csvPath=os.path.join(cwd,"PyPoll","Resources","election_data.csv")
with open(csvPath,newline="") as csvFile:
	csvReader=csv.reader(csvFile,delimiter=',')
	#Skip a line
	next(csvReader)
	#Loop through the rest
	for row in csvReader:
		name=row[2]
		#Check if the name on the row is in the candidates name list, if not add it it.
		if (name not in candidates):
			candidates.append(name)
			candidatesVote.append(1)
		#If it is, then just add 1 more vote under the candidate
		else:
			position=candidates.index(name)
			candidatesVote[position]+=1

	#Find sum of votes
	totalVotes=sum(candidatesVote)
	#Find percentage
	for candidate in candidatesVote:
		candidatePer.append("{:.0%}".format(candidate/totalVotes))
	#Find winner of election 
	winner=candidates[candidatesVote.index(max(candidatesVote))]

#Print in terminal
print("Election Results\n-------------------------\nTotal Votes: "+str(totalVotes)+"\n-------------------------\n")
for i in candidates:
	print(i+":"+str(candidatePer[candidates.index(i)])+" ( "+str(candidatesVote[candidates.index(i)])+")\n")
print("-------------------------\n")
print("Winner: "+winner)


#Print in a text file
txtPath=os.path.join(cwd,"PyPoll","Analysis","analysis.txt")
txtFile=open(txtPath,"w")
txtFile.write("Election Results\n-------------------------\nTotal Votes: "+str(totalVotes)+"\n-------------------------\n")
for i in candidates:
	txtFile.write(i+":"+str(candidatePer[candidates.index(i)])+" ( "+str(candidatesVote[candidates.index(i)])+")\n")
txtFile.write("-------------------------\n")
txtFile.write("Winner: "+winner)
txtFile.close()

