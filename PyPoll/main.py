import os
import csv
totalVotes=0
candidates=[]
candidatesVote=[]
candidatePer=[]


cwd = os.getcwd()
csvPath=os.path.join(cwd,"PyPoll","Resources","election_data.csv")
with open(csvPath,newline="") as csvFile:
	csvReader=csv.reader(csvFile,delimiter=',')
	next(csvReader)
	for row in csvReader:
		name=row[2]
		if (name not in candidates):
			candidates.append(name)
			candidatesVote.append(0)
		else:
			position=candidates.index(name)
			candidatesVote[position]+=1

	totalVotes=sum(candidatesVote)
	for candidate in candidatesVote:
		candidatePer.append("{:.0%}".format(candidate/totalVotes))
	
	winner=candidates[candidatesVote.index(max(candidatesVote))]


print("Election Results\n-------------------------\nTotal Votes: "+str(totalVotes)+"\n-------------------------\n")
for i in candidates:
	print(i+":"+str(candidatePer[candidates.index(i)])+" ( "+str(candidatesVote[candidates.index(i)])+")\n")
print("-------------------------\n")
print("Winner: "+winner)



txtPath=os.path.join(cwd,"PyPoll","Analysis","analysis.txt")
txtFile=open(txtPath,"w")
txtFile.write("Election Results\n-------------------------\nTotal Votes: "+str(totalVotes)+"\n-------------------------\n")
for i in candidates:
	txtFile.write(i+":"+str(candidatePer[candidates.index(i)])+" ( "+str(candidatesVote[candidates.index(i)])+")\n")
txtFile.write("-------------------------\n")
txtFile.write("Winner: "+winner)
txtFile.close()

