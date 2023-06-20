#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period

import os
import csv

#make lists for below to put data inside
profit_change = []
month_count = []
profit = []


# set the path of the file as csvpath
csvpath = os.path.join("Resources", 'budget_data.csv')

with open(csvpath) as csvfile:

    # no need to type delimiter=","
    csvreader = csv.reader(csvfile)

    # set the first row as header
    csvheader = next(csvreader)
    #print(f"Header: {csvheader}") (checking in terminal)

    # add values to the empty lists
    for row in csvreader:
        month_count.append(row[0])
        profit.append(int(row[1]))

    #get a profit change list 
    for i in range(len(profit)-1):
        profit_change.append(profit[i+1]-profit[i])
                      
#evaluate max/min of profit from the profit_change list
increase = max(profit_change)
decrease = min(profit_change)

#find the month of max/min profit change with index function, +1 because the max/min profit change data saved to the previous month
month_increase = profit_change.index(max(profit_change))+1
month_decrease = profit_change.index(min(profit_change))+1

#Print the result, values are the same as instruction
print("")
print("Financial Analysis")
print("------------------------")
print(f"Total Months:{len(month_count)}")
print(f"Total: ${sum(profit)}")
print(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
print(f"Greatest Increase in Profits: {month_count[month_increase]} (${(str(increase))})")
print(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${(str(decrease))})")      


#output the file to txt file
#"\n" to change to next line
output = os.path.join(".", 'output.txt')
with open(output,"w") as outputfile:
    outputfile.write("Financial Analysis")
    outputfile.write("\n")
    outputfile.write("------------------------")
    outputfile.write("\n")
    outputfile.write(f"Total Months:{len(month_count)}")
    outputfile.write("\n")
    outputfile.write(f"Total: ${sum(profit)}")
    outputfile.write("\n")
    #to 2 decimal places
    outputfile.write(f"Average Change: {round(sum(profit_change)/len(profit_change),2)}")
    outputfile.write("\n")
    outputfile.write(f"Greatest Increase in Profits: {month_count[month_increase]} (${str(increase)})")
    outputfile.write("\n")
    outputfile.write(f"Greatest Decrease in Profits: {month_count[month_decrease]} (${str(decrease)})")