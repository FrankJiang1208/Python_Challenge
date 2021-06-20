import os
import csv


cwd = os.getcwd()
csvPath=os.path.join(cwd,"PyPoll","Resources","election_data.csv")
with open(csvPath,newline="") as csvFile:
	csvReader=csv.reader(csvFile,delimiter=',')

	for row in csvReader:
		print(row)

