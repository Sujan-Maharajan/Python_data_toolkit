from dataclasses import dataclass
import csv
from words_to_num import word_into_number
from Level_Two import clean_age, clean_score

@dataclass
class Record:
    id: str
    name: str
    age: int
    city: str
    score: float

class Dataset:
    def __init__(self):
        self.records= []

    def load(self, filename:str) -> None:
        with open(filename,'r') as file:
            read_FILE= csv.DictReader(file)

            for row in read_FILE:
                record= Record(row["id"], row["name"], row["age"], row["city"], row["score"])
                self.records.append(record)

    def calculate_means(self) -> tuple[float, float]:
        valid_age= []
        valid_score= []

        for record in self.records:
            age= clean_age(record.age)

            if age is not None:
                valid_age.append(age)

            score= clean_score(record.score)

            if score is not None:
                valid_score.append(score)

        mean_age= sum(valid_age)/len(valid_age)
        mean_score= sum(valid_score)/len(valid_score)

        return mean_age, mean_score

dataset= Dataset()
dataset.load("messy_people.csv")

mean_age, mean_score= dataset.calculate_means()

print("Mean Age=", mean_age)
print("Mean Score=", mean_score)