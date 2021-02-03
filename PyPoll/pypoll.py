f = open("results.txt","w")
   # printing header for output
print("*************************")
print("Election Results Year 2026")
print("*************************")

# importing csv module 
import csv 
  
# csv file name 
filename = "election_data.csv"
  
# initializing a list for all the rows in the dataset 
rows = [] 

candidatesv = []

# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile, delimiter=',') 
      
    # Ignoring first row for the rest of the calcs 
    fields = next(csvreader) 

    #Initializing variables for counters or other operations   
    votes_counting = 0
    i = 1
    kv = 0
    cv = 0
    lv = 0
    ov = 0 
    # extracting each data row one by one 

    for row in csvreader: 
        rows.append(row) 
    # counting votes for each candidate
        if(str(row[2]) == "Khan"):
            kv = kv + 1
        elif(str(row[2])== "Correy"):
            cv = cv + 1
        elif(str(row[2])== "Li"):
            lv = lv + 1
        elif(str(row[2])== "O'Tooley"):
            ov = ov + 1
        i=i+1
    
    # storing votes for each candidate in a list to determine largest number of votes
    candidatesv = [kv,cv,lv,ov]
    winner = (max(candidatesv))
    
    kv = int(candidatesv[0])
    cv = int(candidatesv[1])
    lv = int(candidatesv[2])
    ov = int(candidatesv[3])


# printing total number of votes by counting each entry
print(f'Total Votes: {len(rows)}') 
print('-------------------')

# Comparing votes for each candidate to determine winner
if ov == winner:
    print(f'Winner is OTooley with {ov} votes')
elif lv == winner:
    print(f'Winner is Li with {lv} votes')
elif cv == winner:
    print(f'Winner is Correy with {cv} votes')
elif kv == winner:
    print(f'Winner is Khan with {kv} votes')    

#calculating votes percentages for each candidate
total = int(len(rows))

kpercentage = kv/total * 100
cpercentage = cv/total * 100
lpercentage = lv/total * 100
opercentage = ov/total * 100

if kpercentage > 50:
    ganador = "Khan"
elif cpercentage > 50:
    ganador = "Correy"
elif lpercentage > 50:
    ganador = "Li"
else:
    ganador = "O'Tooley" 

print('----------------------')
print('Results')

print(f' Khan {kv} votes / {kpercentage} %')
print(f' Correy {cv} votes / {cpercentage} %')
print(f' Li {lv} votes / {lpercentage} %')  
print(f' OTooley {ov} votes / { opercentage} %') 

outputdict ={
    "Total votes": total,
    "Winner" : ganador,
    "Total votes for Khan": kv,
    "Total votes for Correy": cv,
    "Total votes for Li": lv,
    "Total votes for O'Tooley": ov,  
}
f.write(str(outputdict))

f.close()