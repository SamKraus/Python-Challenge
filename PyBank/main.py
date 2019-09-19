# This is main.py in PyBank

import os
import csv

filename = input("budget_data.csv")
month_count = 0
revenue_total = 0 
current_month_revenue = 0
last_month_revenue = 0
revenue_change = 0
revenue_changes = []
months = []

filepath = os.path.join("budget_data.csv")
with open(filepath, "r", newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)


    for row in csvreader:
        month_count = month_count + 1
        months.append(row[0])
        current_month_revenue = int(row[1])
        revenue_total = revenue_total + current_month_revenue
        if month_count > 1:
            revenue_change = current_month_revenue - last_month_revenue
            revenue_changes.append(revenue_change)
        last_month_revenue = current_month_revenue

sum_rev_changes = sum(revenue_changes)
average_change = sum_rev_changes / (month_count - 1)
max_change = max(revenue_changes)
min_change = min(revenue_changes)
max_month_index = revenue_changes.index(max_change)
min_month_index = revenue_changes.index(min_change)
max_month = months[max_month_index]
min_month = months[min_month_index]

print("Financial Analyst")
print("----------------------")
print(f"Total Months: {month_count}")
print(f"Total Revenue: ${revenue_total}")
print(f"Average Revenue Change: ${average_change}")
print(f"Greatest Increase in Revenue: {max_month} (${max_change})")
print(f"Greatest Decrease in Revenue: {min_month} (${min_change})")

save_file = filename.strip(".csv") + "_results.txt"
filepath = os.path.join(".", save_file)
with open(filepath, 'w') as text:
    text.write("Financial Analyst" + "\n")
    text.write("-----------------------------" + "\n")
    text.write(f"Total Months: {month_count}" + "\n")
    text.write(f"Total Revenue: ${revenue_total}" + "\n")
    text.write(f"Average Revenue Change: ${average_change}" + "\n")
    text.write(f"Greatest Increase in Revenue: {max_month} (${max_change})" + "\n")
    text.write(f"Greatest Decrease in Revenue: {min_month} (${min_change})" + "\n")
    

