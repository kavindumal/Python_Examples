import csv

with open('csv_example/customers-100.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    
    for row in reader:
        print(row)
        
print(reader , type(reader))