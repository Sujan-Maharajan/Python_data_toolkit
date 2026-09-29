from Level_Three import Dataset
from Level_Four import average_score, people_per_city, oldest_person, youngest_person

dataset= Dataset()
dataset.load("messy_people.csv")

rows_loaded= len(dataset.records)

dataset.clean()

rows_cleaned= len(dataset.records)
rows_dropped= rows_loaded - rows_cleaned

total_dropped= sum(dataset.drop_reasons.values())

print("Rows loaded:", rows_loaded)
print("Rows cleaned:", rows_cleaned)
print("Rows dropped:", rows_dropped)
print("Total dropped from reasons:", total_dropped)
print("Drop reasons:", dataset.drop_reasons)
print("\n")
average= average_score(dataset)
cities= people_per_city(dataset)
oldest= oldest_person(dataset)
youngest= youngest_person(dataset)

print("\nAverage Score:", average)
print("People per city:", cities)
print("Oldest person:", oldest)
print("Youngest person:", youngest)