import os
import csv

bank_csv = os.path.join('Resources', "budget_data.csv")

with open(bank_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    print("Financial Analysis")
    print("--------------------------------")   

# find total number of months included in dataset
    bank_list = list(csvreader)
    # print(bank_list)
    total_months = len(bank_list)
    print("Total Months: " + str(total_months)) 
    
# find the net total of "Profits/Losses" over the entire period 
with open(bank_csv,newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    sum_total = 0
    for row in csvreader:
        sum_total = sum(int(row[1]) for row in csvreader)
        formatted_sum = '${}'.format(sum_total)
        print("Total: " + str(formatted_sum))

date_list, PL_list = map(list, zip(*bank_list))

PL_list = list(map(int, PL_list))

diff = [j - i for i, j in zip(PL_list[: -1], PL_list[1 :])] 

# def Average(diff): 
avg_change = float((sum(diff) / len(diff)))
avg_formatted = '${:.2f}'.format(avg_change)
print("Average Change: " + str(avg_formatted))

max_increase = (max(diff))
max_inc_formatted = '${}'.format(max_increase)

date_inc = (date_list[diff.index(max(diff))+1])
print("Greatest Increase in Profits: " + date_inc + " " + "(" + str(max_inc_formatted) +")")
max_decrease = (min(diff))
max_dec_formatted = '${}'.format(max_decrease)

date_dec = (date_list[diff.index(min(diff))+1])
print("Greatest Decrease in Profits: " + date_dec + " " + "(" + str(max_dec_formatted) + ")")