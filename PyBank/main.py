import os
import csv

totalMonth=0
totalProfitLoss=0
aveProfitLoss=0
maxProfit=0
maxProfitDate=""
maxLoss=0
maxLossDay=""


cwd = os.getcwd()
csvPath=os.path.join(cwd,"PyBank","Resources","budget_data.csv")
with open(csvPath,newline="") as csvFile:
	csvReader=csv.reader(csvFile,delimiter=',')

	for row in csvReader:
		if (row[0]=="Date"):
			continue
		else:
			totalMonth+=1
			totalProfitLoss+=int(row[1])
			if(int(row[1])>maxProfit):
				maxProfit=int(row[1])
				maxProfitDate=row[0]
			elif(int(row[1])<maxLoss):
				maxLoss=int(row[1])
				maxLossDate=row[0]
	
	
	aveProfitLoss=totalProfitLoss/totalMonth
print("Financial_Analysis\n")
print("---------------------------\n")
print("There are "+ str(totalMonth)+" months in the budget\n")
print("Total Revenues/Loss of $"+str(totalProfitLoss)+".\n" )
print("The average revenue/loss change was $"+str(aveProfitLoss)+" per month.\n")
print("The maximum change in revenue was $"+str(maxProfit)+" in "+maxProfitDate+"\n")
print("The minimum change in revenue was $"+str(maxLoss)+" in "+maxLossDate+"\n")




txtPath=os.path.join(cwd,"PyBank","Analysis","analysis.txt")
txtFile=open(txtPath,"w")
txtFile.write("Financial_Analysis\n")
txtFile.write("---------------------------\n")
txtFile.write("There are "+ str(totalMonth)+" months in the budget\n")
txtFile.write("Total Revenues/Loss of $"+str(totalProfitLoss)+".\n" )
txtFile.write("The average revenue/loss change was $"+str(aveProfitLoss)+" per month.\n")
txtFile.write("The maximum change in revenue was $"+str(maxProfit)+" in "+maxProfitDate+"\n")
txtFile.write("The minimum change in revenue was $"+str(maxLoss)+" in "+maxLossDate+"\n")
txtFile.close()