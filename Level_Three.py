from dataclasses import dataclass
import csv
from words_to_num import word_into_number
from Level_Two import clean_age, clean_score, clean_city, clean_name

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

    def clean(self) -> None:
        mean_age, mean_score= self.calculate_means()

        cleaned_records= []
        seen_ids= set()

        for record in self.records:

            if record.id.strip()=="":
                continue

            if record.id in seen_ids:
                continue

            age= clean_age(record.age,mean_age)

            if age is None:
                continue

            score= clean_score(record.score,mean_score)

            if score is None:
                continue

            record.age= age
            record.score= score
            record.name= clean_name(record.name)
            record.city= clean_city(record.city)

            seen_ids.add(record.id)
            cleaned_records.append(record)

        self.records= cleaned_records

    def stream_clean(self):
        for record in self.records:
            yield record

    def stream_file(self, filename:str):
        with open(filename,'r') as file:
            read_FILE= csv.DictReader(file)

            for row in read_FILE:
                yield row

dataset= Dataset()
# dataset.load("messy_people.csv")
# dataset.clean()

# print("Cleaned Records:", len(dataset.records))

# for record in dataset.stream_clean():
#     print(record)

for row in dataset.stream_file("messy_people.csv"):
    print(row)