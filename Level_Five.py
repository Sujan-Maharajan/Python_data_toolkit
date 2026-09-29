from Level_Three import Dataset

dataset= Dataset()
dataset.load("messy_people.csv")

rows_loaded= len(dataset.records)

dataset.clean()

rows_cleaned= len(dataset.records)
rows_dropped= rows_loaded - rows_cleaned