from Level_Three import Dataset
from Level_Four import average_score, people_per_city, oldest_person, youngest_person
from report import create_report

dataset= Dataset()
dataset.load("messy_people.csv")
rows_loaded= len(dataset.records)
dataset.clean()

rows_cleaned= len(dataset.records)
rows_dropped= rows_loaded - rows_cleaned

print("Analysis timing:")
average= average_score(dataset)
cities= people_per_city(dataset)
oldest= oldest_person(dataset)
youngest= youngest_person(dataset)

print("\n")

report = create_report(rows_loaded, rows_cleaned, rows_dropped, dataset.drop_reasons, average, cities, oldest, youngest)
print (report)

with open ("report.txt","w") as file:
    file.write(report)