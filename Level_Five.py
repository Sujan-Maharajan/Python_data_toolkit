from Level_Three import Dataset

dataset= Dataset()
dataset.load("messy_people.csv")

rows_loaded= len(dataset.records)

dataset.clean()

print("Drop reasons:", dataset.drop_reasons)

rows_cleaned= len(dataset.records)
rows_dropped= rows_loaded - rows_cleaned

total_dropped= sum(dataset.drop_reasons.values())
print("Rows loaded:", rows_loaded)
print("Rows cleaned:", rows_cleaned)
print("Rows dropped:", rows_dropped)
print("Total dropped from reasons:", total_dropped)