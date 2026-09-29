from Level_One import Record
from Level_Three import Dataset
import time

def log_time(func):
    def wrapper(*args,**kwargs):
        start_time= time.time()

        result= func(*args,**kwargs)

        end_time= time.time()

        print(f"{func.__name__} took {end_time - start_time:.6f} seconds")

        return result

    return wrapper

@log_time
def average_score(dataset: Dataset) -> float:
    total_score= 0

    for record in dataset.records:
        total_score+= record.score
    average= total_score/ len(dataset.records)

    return average

@log_time
def people_per_city(dataset: Dataset) -> dict:
    city_count= {}

    for record in dataset.records:
        city= record.city

        if city not in city_count:
            city_count[city]= 1
        else:
            city_count[city]+=1
    return city_count

@log_time
def oldest_person(dataset: Dataset) -> Record:
    oldest_person= dataset.records[0]

    for record in dataset.records:
        if record.age > oldest_person.age:
            oldest_person= record

    return oldest_person

@log_time
def youngest_person(dataset: Dataset) -> Record:
    youngest_person= dataset.records[0]

    for record in dataset.records:
        if record.age < youngest_person.age:
            youngest_person= record

    return youngest_person

if __name__ == "__main__":
    dataset= Dataset()
    dataset.load("messy_people.csv")
    dataset.clean()

    print("Average Score:",average_score(dataset))
    print("People per city:", people_per_city(dataset))
    print("Oldest person:",oldest_person(dataset))
    print("Youngest person:",youngest_person(dataset))