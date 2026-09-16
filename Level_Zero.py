import csv

with open('messy_people.csv','r') as file:
    read_FILE= csv.DictReader(file)
    data= list(read_FILE)
    print("Rows=",len(data))
    print("First 3 rows=",data[0:3])
