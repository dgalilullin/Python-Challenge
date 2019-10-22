import os
import csv
#csv_path = os.path.join("..","Resources","budget_data.csv")
#csv_path = os.path.join("C:","Users","dgali","Desktop","budget_data.csv")
#
csv_path =r"C:\Users\dgali\Documents\GitHub\Python-Challenge\PyBank\budget_data.csv"
with open (csv_path, newline="") as csvfile:
    rows = csv.reader (csvfile,delimiter=",")
    #lst = list (rows)
    #print (lst)
    my_dict = dict()
    for row in rows:
        key =row [0]
        value = row [1]
        my_dict [key] = value
    dates = list(my_dict.keys())
    amount = list(my_dict.values())    
    dates.pop (0)
    amount.pop (0)
    amount = list(map(int, amount))
    total_months = len(dates)
    total_profit_loss = sum(amount)
    max_amount = max(amount)
    min_amount = min(amount)
    max_index = amount.index(max_amount)
    min_index = amount.index(min_amount)
    max_date = dates[max_index]
    min_date = dates[min_index]
    print ("Total months:", total_months)
    print("Total:", total_profit_loss)
    print("Greatest Increase in Profits:" , max_date, max_amount)
    print("Greatest Decrease in Profits:" , min_date,min_amount)
f = open(r"C:\Users\dgali\Documents\GitHub\Python-Challenge\PyBank\summary.txt",'w')
f.write ("Total months: "+str(total_months)+"\n")
f.write ("Total: "+ str(total_profit_loss)+"\n")
f.write ("Greatest Increase in Profits: " +str(max_date)+" "+ str(max_amount)+"\n")
f.write ("Greatest Decrease in Profits: " + str(min_date)+" "+ str(min_amount))
f.close()
