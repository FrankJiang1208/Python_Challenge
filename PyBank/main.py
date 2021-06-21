#Import all library needed
import os
import csv
from csv import reader

#Set all variable needed
totalMonth=0
totalProfitLoss=0
aveProfitLoss=0
maxProfit=0
maxProfitDate=""
maxLoss=0
maxLossDay=""
totalChange=0
aveChange=0

#Find path to csv file needed
cwd = os.getcwd()
csvPath=os.path.join(cwd,"PyBank","Resources","budget_data.csv")

#Open file
with open(csvPath,newline="") as csvFile:
	#Assign reader
	csvReader=csv.reader(csvFile,delimiter=',')
	next(csvReader)
	#Loop through every row
	for row in csvReader:
		#Make sure its not the first row
		#Increment month count
		totalMonth+=1
		#Add this month earning/loss to total
		totalProfitLoss+=int(row[1])
			
		#Find max and min
		if(int(row[1])>maxProfit):
			maxProfit=int(row[1])
			maxProfitDate=row[0]
		elif(int(row[1])<maxLoss):
			maxLoss=int(row[1])
			maxLossDate=row[0]
	aveProfitLoss=totalProfitLoss/totalMonth

#Calculate average
with open(csvPath,newline="") as csvFile:
	#Assign reader
	csvReader=csv.reader(csvFile,delimiter=',')
	fileList=list(csv.reader(csvFile, delimiter=','))
	length=len(fileList)
	totalChange=int(fileList[1:2][0][1])-int(fileList[length-1:length][0][1])
	aveChange=totalChange/totalMonth
	

#Print out on terminal
print("Financial_Analysis\n")
print("---------------------------\n")
print("There are "+ str(totalMonth)+" months in the budget\n")
print("Total Revenues/Loss of $"+str(totalProfitLoss)+".\n" )
print("The average revenue/loss change was $"+str(aveChange)+" per month.\n")
print("The maximum change in revenue was $"+str(maxProfit)+" in "+maxProfitDate+"\n")
print("The minimum change in revenue was $"+str(maxLoss)+" in "+maxLossDate+"\n")



#Write on a text file
txtPath=os.path.join(cwd,"PyBank","Analysis","analysis.txt")
txtFile=open(txtPath,"w")
txtFile.write("Financial_Analysis\n")
txtFile.write("---------------------------\n")
txtFile.write("There are "+ str(totalMonth)+" months in the budget\n")
txtFile.write("Total Revenues/Loss of $"+str(totalProfitLoss)+".\n" )
txtFile.write("The average revenue/loss change was $"+str(aveChange)+" per month.\n")
txtFile.write("The maximum change in revenue was $"+str(maxProfit)+" in "+maxProfitDate+"\n")
txtFile.write("The minimum change in revenue was $"+str(maxLoss)+" in "+maxLossDate+"\n")
txtFile.close()