from dataclasses import dataclass
import csv
from typing import Iterator
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
        self.records=[]
        self.drop_reasons={}

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

    def calculate_file_means(self, filename:str) -> tuple[float, float]:
        valid_age= []
        valid_score= []

        with open(filename,'r') as file:
            read_FILE= csv.DictReader(file)

            for row in read_FILE:
                age= clean_age(row["age"])

                if age is not None:
                    valid_age.append(age)

                score= clean_score(row["score"])

                if score is not None:
                    valid_score.append(score)

        mean_age= sum(valid_age)/len(valid_age)
        mean_score= sum(valid_score)/len(valid_score)

        return mean_age, mean_score

    def clean(self) -> None:
        self.drop_reasons={}

        mean_age, mean_score= self.calculate_means()

        cleaned_records=[]
        seen_ids= set()

        for record in self.records:

            if record.id.strip()=="":
                self.drop_reasons["empty id"]= self.drop_reasons.get("empty id", 0)+ 1
                continue

            if record.id in seen_ids:
                self.drop_reasons["duplicate id"]= self.drop_reasons.get("duplicate id", 0)+ 1
                continue

            age= clean_age(record.age,mean_age)

            if age is None:
                self.drop_reasons["invalid age"]= self.drop_reasons.get("invalid age", 0)+ 1
                continue

            score= clean_score(record.score,mean_score)

            if score is None:
                self.drop_reasons["invalid score"]= self.drop_reasons.get("invalid score", 0)+ 1
                continue

            record.age= age
            record.score= score
            record.name= clean_name(record.name)
            record.city= clean_city(record.city)

            seen_ids.add(record.id)
            cleaned_records.append(record)

        self.records= cleaned_records

    def stream_file(self, filename:str) -> Iterator[Record]:
        mean_age, mean_score= self.calculate_file_means(filename)

        seen_ids= set()

        with open(filename,'r') as file:
            read_FILE= csv.DictReader(file)

            for row in read_FILE:
                record= Record(row["id"], row["name"], row["age"], row["city"], row["score"])

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

                yield record

dataset = Dataset()

if __name__== "__main__":
    print("Records are:")
    for record in dataset.stream_file("messy_people.csv"):
        print(record)