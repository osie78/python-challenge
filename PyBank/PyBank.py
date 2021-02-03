#creates summary.txt file for output
f = open("summary.txt","w")

# printing header for output
print("Financial Analysis")
print("------------------------")

# importing csv module 
import csv 
  
# csv file name 
filename = "budget_data.csv"
  
# initializing a list for all the rows in the dataset 
rows = [] 
delta = [] 
pl=[]
months =[]

# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # Ignoring first row for the rest of the calcs 
    fields = next(csvreader) 

    #Initializing variables for counters or other operations   
    profit_losses = 0
    di = 0
    i = 0
    deltachange = 0
    
    # extracting each data row one by one 
    for row in csvreader: 
        
        rows.append(row) 
        profit_losses = int(row[1]) + profit_losses
        
        #creating a new list for profit and losses only
        a = int(row[1])
        pl.append(a)

        #creating a new list for months and years
        b = str(row[0])
        months.append(b)
        
        i=i+1

    # I have created 3 separate lists: one for profit&losses, one for months and one for the delta of p&l

    # get total number of rows in the file as total of months of data
     
    nor=int(csvreader.line_num) 
    
    #In this loop, the list delta for p&l is being populated. 
    for x in range(1,len(pl)):
        d = [int(pl[x])-int(pl[x-1])]    
        delta.append(d)
    
    # total delta is calculated
    j = 0
    for y in delta:
        deltachange = int(y[0]) + deltachange
        j=j+1

    #average of delta is calculated as:
    average = deltachange / (len(delta))

    #from the list delta p&l maximum and minimum are calculated as "Greatest increase" and "Greatest decrease"
    increase = (max(delta))
    decrease = (min(delta))

#The following indexation looks for the corresponding position for min and max in the list "delta". However,  
#since the list delta has on offset of 1 vs the lists p&l and months, 1 must be added. These indexes result in the months for min and max

indicemax=int(delta.index(increase)) + 1
indicemin=int(delta.index(decrease)) + 1
   
     
#printing the results

print(" There are " + str(nor -1) + " months in this analysis")
print(" The total profit and losses are " + str(profit_losses))
print(f' The total change was {deltachange} with an average change of {"%.2f" % average} ' )
print(f' Greatest Increase in Profits was {increase} in {months[indicemax]} ')
print(f' Greates decrease in Profits was {decrease} in {months[indicemin]} ' )

f.write(" There are " + str(nor -1) + " months in this analysis" "\n")
f.write(" The total profit and losses are " + str(profit_losses) + "\n")
f.write(" The total change was " + str(deltachange) + " with an average change of " + str("%.2f" % average) + "\n")
f.write(" Greatest Increase in Profits was " + str(increase) + " in " + str(months[indicemax]) + "\n")
f.write(" Greates decrease in Profits was " + str(decrease) + " in " + str(months[indicemin]))


f.close()



